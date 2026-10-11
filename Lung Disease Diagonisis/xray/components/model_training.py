import os
import sys

import joblib
import torch
from torch.nn import functional, CrossEntropyLoss, Module
from torch.optim import Optimizer

from xray.entity.artifacts_entity import DataTransformationArtifacts, ModelTrainerArtifacts
from xray.entity.config_entity import ModelTrainerConfig

from xray.exception import XrayException

from tqdm import tqdm

from xray.constants.train_pipeline_constant import *

from torch.optim.lr_scheduler import StepLR, _LRScheduler

from xray.model.architecture import NeuralNetwork

"""

self.model_trainer_config: ModelTrainerConfig = model_trainer_config
#                         ↑
#                    expected type
# 
                         vs

       self.model_trainer_config = model_trainer_config   

In short: the type annotation isn't required; 
it's there to make the code more explicit and maintainable. 
Both versions assign the value to the instance.                     
"""


class ModelTraining():
    def __init__(self,
                data_transformation_artifacts: DataTransformationArtifacts,
                model_trainer_config: ModelTrainerConfig):

        self.data_transformation_artifacts: DataTransformationArtifacts = data_transformation_artifacts
        self.model_trainer_config:ModelTrainerConfig = model_trainer_config

        self.model: Module = NeuralNetwork()

        self.loss_fn = torch.nn.CrossEntropyLoss()
        


    def Train(self, optimizer: Optimizer):
        """
                Description: To train the model
        
                input: model,device,train_loader,optimizer,epoch
        
                output: loss, batch id and accuracy

         """

        try:
            self.model.train()

            correctly_pred: int = 0
            processed: int = 0

            progress_bar = tqdm(self.data_transformation_artifacts.transformed_train_obj)


            for batch_indx, (images, target) in enumerate(progress_bar):
                images = images.to(DEVICE)
                target = target.to(DEVICE)


                self.optimizer.zero_grad()

                y_pred = self.model(images)


                loss = self.loss_fn(y_pred, target)
                loss.backward()


                self.optimizer.step()


                prediction = y_pred.argmax(dim = 1, keepdim = True)
                correctly_pred += prediction.eq(target.view_as(prediction)).sum().item()


                processed += len(images)

                progress_bar.set_description(desc=f'loss = {loss.item()} Batchid = {batch_indx}, Accuracy = {100*correctly_pred/processed:0.2f}')

        except Exception as e:
            raise XrayException(e, sys)



    def Test(self) -> None:
        try:
            
            self.model.eval()
            test_loss = 0
            correct_pred = 0   

            with torch.no_grad(): 

              for images, target in enumerate(self.data_transformation_artifacts.transformed_test_obj):
                  images = images.to(DEVICE)
                  target = target.to(DEVICE)  

                  y_pred = self.model(images)

                  loss = self.loss_fn(y_pred, target)
                  test_loss += loss.item()

                  prediction = y_pred.argmax(dim=1, keepdim=True)
                  correct_pred += prediction.eq(target.view_as(prediction)).sum().item()


            test_loss /= len(self.data_transformation_artifacts.transformed_test_obj.dataset) # basically it is dividing all the accumulated loss by the length of test_loader => gives average loss per batch
            print(f"Test error: \n Accuracy: {100.*correct_pred / len(self.data_transformation_artifacts.transformed_test_obj.dataset)} %,  Avg loss: {test_loss:0.2f}\n")      

                      

        except Exception as e:
            raise XrayException(e, sys)




            
            
    def initiate_model_trainer(self) -> ModelTrainerArtifacts:
        try:
            # assigning model to device 
            model: Module = self.model.to(self.model_trainer_config.device)

            # providing optimizer
            optimizer: Optimizer = torch.optim.SGD(model.parameters(), **self.model_trainer_config.optimizer_params)

            # providing sceduler
            scheduler: _LRScheduler = StepLR(
                            optimizer=optimizer, **self.model_trainer_config.optimizer_params)


            for i in range (1, self.model_trainer_config.epoch+1):
                print("EPOCH: ", i)

                self.Train(optimizer=optimizer)
                optimizer.step()
                scheduler.step()

                self.Test()

            os.makedirs(self.model_trainer_config.artifact_dir, exist_ok=True)   
            torch.save(model, self.model_trainer_config.trained_model_path) 


            train_transforms_obj = joblib.load(
                            self.data_transformation_artifacts.train_dataloader_filepath
                        )
            model_trainer_artifact: ModelTrainerArtifacts = ModelTrainerArtifacts(
                            trained_model_path=self.model_trainer_config.trained_model_path
                        )

            return model_trainer_artifact

        except Exception as e:
            raise XrayException(e, sys)
