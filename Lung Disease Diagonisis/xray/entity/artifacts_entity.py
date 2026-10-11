"""
When you hear: "artifact"
don't automatically think: "file on my computer."

An artifact can be:

a file path
a DataLoader
a model path
an accuracy value
a configuration
a trained model
metadata
multiple pieces of information grouped together

WHY NOT USE DICTONARIES?
artifacts give you a cleaner, more structured approach:

A SIMPLE PIPELINE COULD BE 
                 DATA INGESTION
                       │
                       │
                       ▼
            DataIngestionArtifact
            ┌────────────────────┐
            │ train_file_path    │
            │ test_file_path     │
            └────────────────────┘
                       │
                       ▼
              DATA TRANSFORMATION
                       │
                       │
                       ▼
          DataTransformationArtifact
          ┌──────────────────────────┐
          │ train DataLoader         │
          │ test DataLoader          │
          │ train transform path     │
          │ test transform path      │
          └──────────────────────────┘
                       │
                       ▼
                 MODEL TRAINING
                       │
                       │
                       ▼
             ModelTrainerArtifact
             ┌────────────────────┐
             │ trained_model_path │
             └────────────────────┘
                       │
                       ▼
               MODEL EVALUATION
                       │
                       │
                       ▼
          ModelEvaluationArtifact
          ┌──────────────────────┐
          │ model_accuracy        │
          └──────────────────────┘
                       │
                       ▼
                 MODEL PUSHING
                       │
                       │
                       ▼
             ModelPusherArtifact
             ┌─────────────────────┐
             │ bentoml_model_name  │
             │ bentoml_service_name│
             └─────────────────────┘

The artifact class definitions don't actually perform the ML work.
doesn't train anything.

It only defines what information the model-training stage should return.
The actual training might happen somewhere else:  

Artifacts are structured containers used to store and pass the outputs of different stages of an ML pipeline,
 making the pipeline organized, modular, maintainable,
   and easy for different components to communicate with each other.

"""




## An artifact is an object that stores the output/result of one stage of your ML pipeline so that the next stage can use it.
from dataclasses import dataclass
from torch.utils.data import dataloader



@dataclass    ##dataclass is a Python feature that makes it easier to create classes whose main purpose is storing dat
class DataIngestionArtifacts: ## outputs produced by the Data Ingestion stage
      train_data_filepath = str
      test_data_filepath = str
   


@dataclass
class DataTransformationArtifacts:
      transformed_train_obj = dataloader ##This is your transformed training DataLoader
      transformed_test_obj = dataloader
   

      train_dataloader_filepath = str ## store the location of a saved training transformation configuration/object.
      test_dataloader_filepath = str


@dataclass
class ModelTrainerArtifacts:
      trained_model_path = str ## After training, you might save the model:



@dataclass
class ModelEvaluationArtifacts:
      model_accuracy = float     
                   