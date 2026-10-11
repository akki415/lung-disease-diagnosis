import sys
from typing import Tuple

import torch
from torch.nn import CrossEntropyLoss, Module
from torch.optim import SGD, Optimizer
from torch.utils.data import DataLoader

from xray.entity.artifacts_entity import (
    DataTransformationArtifacts,
    ModelEvaluationArtifacts,
    ModelTrainerArtifacts,
)
from xray.entity.config_entity import ModelEvaluationConfig
from xray.exception import XRayException
from xray.model.architecture import NeuralNetwork


class ModelEvaluation:
    def __init__(
        self,
        data_transformation_artifact: DataTransformationArtifacts,
        model_evaluation_config: ModelEvaluationConfig,
        model_trainer_artifact: ModelTrainerArtifacts,
    ):

        self.data_transformation_artifact = data_transformation_artifact

        self.model_evaluation_config = model_evaluation_config

        self.model_trainer_artifact = model_trainer_artifact

    def configuration(self) -> Tuple[DataLoader, Module, float, Optimizer]:
        

        try:
            test_dataloader: DataLoader = (
                self.data_transformation_artifact.transformed_test_obj
            )

            model: Module = NeuralNetwork()

            model: Module = torch.load(self.model_trainer_artifact.trained_model_path)

            model.to(self.model_evaluation_config.device)

            cost: Module = CrossEntropyLoss()

            optimizer: Optimizer = SGD(
                model.parameters(), **self.model_evaluation_config.optimizer_params
            )

            model.eval()


            return test_dataloader, model, cost, optimizer

        except Exception as e:
            raise XRayException(e, sys)

    def test_net(self) -> float:

        try:
            test_dataloader, net, cost, _ = self.configuration()

            with torch.no_grad():
                holder = []

                for _, data in enumerate(test_dataloader):
                    images = data[0].to(self.model_evaluation_config.device)

                    labels = data[1].to(self.model_evaluation_config.device)

                    output = net(images)

                    loss = cost(output, labels)

                    predictions = torch.argmax(output, 1)

                    for i in zip(images, labels, predictions):
                        h = list(i)

                        holder.append(h)

                
                    

                    self.model_evaluation_config.test_loss += loss.item()

                    self.model_evaluation_config.test_accuracy += (
                        (predictions == labels).sum().item()
                    )

                    self.model_evaluation_config.total_batch += 1

                    self.model_evaluation_config.total += labels.size(0)


            accuracy = (
                self.model_evaluation_config.test_accuracy
                / self.model_evaluation_config.total
            ) * 100

            

            return accuracy

        except Exception as e:
            raise XRayException(e, sys)

    def initiate_model_evaluation(self) -> ModelEvaluationArtifacts:



        try:
            accuracy = self.test_net()

            model_evaluation_artifact: ModelEvaluationArtifacts = (
                ModelEvaluationArtifacts(model_accuracy=accuracy)
            )

            

            return model_evaluation_artifact

        except Exception as e:
            raise XRayException(e, sys)
