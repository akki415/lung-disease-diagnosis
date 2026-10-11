"""            

             config_entity.py
                    │
                    │ creates
                    ▼
          DataIngestionConfig
                    │
                    │ contains
                    ▼
       ┌─────────────────────────┐
       │ bucket_name              │
       │ s3_data_folder           │
       │ artifact_dir             │
       │ data_path                │
       │ train_data_path          │
       │ test_data_path           │
       └─────────────────────────┘
                    │
                    │ passed to
                    ▼
             data_ingestion.py
                    │
                    ▼
             DataIngestion
                    │
                    ▼
             S3Operation
                    │
                    ▼
              AWS S3 → Local

## it will happen for all the pipeline steps  
# DataIngestionConfig tells DataIngestion what to do and where to put things. DataIngestion actually performs the operation  
# 
# 
# artifact_dir is a parent/root folder for the outputs of one pipeline run.
#  The paths you create under it are not themselves "stored" inside artifact_dir; 
# rather, they point to folders that are located inside artifact_dir    

artifact/
└── 2026_09_14_17_00_00/
    │
    ├── data_ingestion/
    │   └── data/
    │
    ├── data_transformation/
    │   ├── train/
    │   └── test/
    │
    └── model_trainer/
        └── model/


And the timestamp is particularly important

Imagine you run your pipeline three times:

artifact/
│
├── 2026_09_12_10_00_00/
│   ├── data_ingestion/
│   ├── data_transformation/
│   └── model_trainer/
│
├── 2026_09_13_15_30_00/
│   ├── data_ingestion/
│   ├── data_transformation/
│   └── model_trainer/
│
└── 2026_09_14_17_00_00/
    ├── data_ingestion/
    ├── data_transformation/
    └── model_trainer/              
              
"""


import os
from torch import device
from dataclasses import dataclass
from xray.constants.train_pipeline_constant import *


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.s3_data_folder: str = S3_DATA_FOLDER  # in constant _init__ file we S3_DATA_FOLDER = data
        self.bucket_name: str = BUCKET_NAME

        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP) # artifacts/2026_09_12_10_00_00/

        self.data_path: str = os.path.join(self.artifact_dir, "data_ingestion", self.s3_data_folder)  # artifacts/timestamp/data_ingestion/data
        self.train_data_path :str = os.path.join(self.data_path, "train")
        self.test_data_path: str = os.path.join(self.data_path, "test")



@dataclass
class DataTransformationConfig:
    # here we will need dataloaders, jitter, resize, rotation, horizontal flip
    # normalization, tensor 

    def __init__(self):
        self.color_jitter_transform: dict[str, float] = {    # even if not [str, float] during runtime python will hunt for const values and will know as str & float
            "saturation" : SATURATION,
            "hue": HUE,
            "brightness": BRIGHTNESS,
            "contrast": CONTRAST
        }

        self.resize: int = RESIZE
        self.center_crop: int = CENTERCROP
        self.random_rotation: int = RANDOMROTATION

        self.normalise_transforms: dict = {
            "mean": NORMALIZE_LIST_1,
            "std": NORMALIZE_LIST_2

        }

        self.data_loder: dict={
            "shuffle": SHUFFLE,
            "batch_size" : BATCH_SIZE,
            "pin_memory": PIN_MEMORY
        }

        # now we have to do transforming so need folder/directiory to point to it
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP, "data_transformation")

        self.train_transform_file: str = os.path.join(self.artifact_dir, TRAIN_TRANSFORMS_FILE)
        self.test_transform_file: str = os.path.join(self.artifact_dir, TEST_TRANSFORMS_FILE)



@dataclass
class ModelTrainerConfig:
    def __init__(self):
        # we will need {trained model name // trained model path //}

        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP, TRAINED_MODEL_DIR)

        self.trained_model_path: str = os.path.join(self.artifact_dir, TRAINED_MODEL_NAME)

        self.device: device = DEVICE

        
        self.train_transforms_key: str = TRAIN_TRANSFORMS_KEY

        self.optimizer_params: dict = {"lr":0.001, "momentum":0.9}
        self.scheduler_params: dict = {"step_size": STEP_SIZE, "gamma":GAMMA}

        self.epoch: int = EPOCH




@dataclass
class ModelEvaluationConfig:
    def __init__(self):
        self.device: device = DEVICE
        
        self.test_loss: int = 0
        
        self.test_accuracy: int = 0
        
        self.total: int = 0
        
        self.total_batch: int = 0
        
        self.optimizer_params: dict = {"lr": 0.01, "momentum": 0.8}
            
