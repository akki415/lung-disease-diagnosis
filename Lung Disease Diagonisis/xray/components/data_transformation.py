import os
import sys
import joblib

from xray.entity.artifacts_entity import DataTransformationArtifacts, DataIngestionArtifacts
from xray.entity.config_entity import DataTransformationConfig

from xray.constants.train_pipeline_constant import *

from xray.exception import XrayException

from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, Dataset

"""Raw X-ray images
       │
       ▼
Training images ──► Resize
                  ► CenterCrop
                  ► ColorJitter
                  ► RandomFlip
                  ► RandomRotation
                  ► ToTensor
                  ► Normalize
                       │
                       ▼
                 Training DataLoader
                       │
                       ▼
                    Model


   Images
   ↓
DataTransformation
   ↓
Clean/preprocessed images
   ↓
DataLoader
   ↓
Neural Network  



What is transforms.Compose?
train_transform = transforms.Compose(
    [
        transformation1,
        transformation2,
        transformation3,
    ]
)

Think of it like a pipeline.
For example:

transforms.Compose([
    Resize,
    Crop,
    Flip,
    Tensor,
    Normalize
])

 ## This serializes the training transformation object and saves it to disk
                train_transform
                        ↓
                   joblib.dump()
                        ↓
                 train_transform.pkl 
                 Why save it?

This is important in an ML pipeline.

Imagine you train a model today and later deploy it.

You need to apply the exact same preprocessing to new data.
"""                 


class DataTransformation:
    def __init__(self, 
                data_transformation_config: DataTransformationConfig,
                data_integration_artifacts: DataIngestionArtifacts) -> None:

          self.data_transformation_config = data_transformation_config
          self.data_integration_artifacts = data_integration_artifacts



    def transforming_training_data(self) -> transforms.Compose:

        try:
            train_transform: transforms.Compose = transforms.Compose([

                transforms.Resize(self.data_transformation_config.resize),
                transforms.CenterCrop(self.data_transformation_config.center_crop),
                transforms.ColorJitter(**self.data_transformation_config.color_jitter_transform),
                transforms.Normalize(**self.data_transformation_config.normalise_transforms),
                transforms.RandomRotation(self.data_transformation_config.random_rotation),
                transforms.ToTensor(),
                transforms.RandomHorizontalFlip()

                  
             ])

            return train_transform
        except Exception as e:
            raise XrayException(e, sys)



    def transforming_testing_data(self)-> transforms.Compose:

        try:
            test_transform: transforms.Compose = transforms.Compose([
                transforms.Resize(self.data_transformation_config.resize),
                transforms.CenterCrop(self.data_transformation_config.center_crop),
                transforms.ToTensor(),
                transforms.Normalize(**self.data_transformation_config.normalise_transforms)
            ]) 

            return test_transform
        except Exception as e:
            raise XrayException(e, sys)   




    def data_loader(self,
                    train_transform: transforms.Compose,
                    test_transform: transforms.Compose) -> tuple[DataLoader, DataLoader]:  

        try:
            train_data: Dataset = ImageFolder(
                os.path.join(self.data_integration_artifacts.train_data_filepath), transform=train_transform
            )

            test_data: Dataset = ImageFolder(
                os.path.join(self.data_integration_artifacts.test_data_filepath), transform=test_transform
            )

            train_loader: DataLoader = DataLoader(
                train_data, **self.data_transformation_config.data_loder
            )

            test_loader:  DataLoader = DataLoader(
                test_data, **self.data_transformation_config.data_loder
            )

        except Exception as e:
            raise XrayException(e, sys)



    def initiate_data_transformation(self) -> DataTransformationArtifacts:

        try:
            train_transform: transforms.Compose = self.transforming_training_data() ## calling mthd
            
            test_transform: transforms.Compose = self.transforming_testing_data()
            
            os.makedirs(self.data_transformation_config.artifact_dir, exist_ok=True)
            
            joblib.dump(
               

                            train_transform, self.data_transformation_config.train_transforms_file
                        )
            
            joblib.dump(
                            test_transform, self.data_transformation_config.test_transforms_file
                        )
            
            train_loader, test_loader = self.data_loader(
                            train_transform=train_transform, test_transform=test_transform
                        )
            
            data_transformation_artifact: DataTransformationArtifacts = DataTransformationArtifacts(
                            transformed_train_object=train_loader,
                            transformed_test_object=test_loader,
                            train_transform_file_path=self.data_transformation_config.train_transforms_file,
                            test_transform_file_path=self.data_transformation_config.test_transforms_file,
                        )


            return data_transformation_artifact
            
        except Exception as e:
            raise XrayException(e, sys)
            
            
            