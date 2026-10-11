import os
import sys

from xray.exception import XrayException
from xray.cloud_storage.s3operation import S3Operations

from xray.constants.train_pipeline_constant import *


from xray.entity.artifacts_entity import DataIngestionArtifacts
from xray.entity.config_entity import DataIngestionConfig

"""Its job is essentially:

        Amazon S3
            │
            │ download
            ▼
      Local data folder
            │
            ▼
    Locate train/test data
            │
            ▼
   Create DataIngestionArtifact  (what would be the output)
            │
            ▼
     Return file paths

So this class doesn't actually perform machine-learning training.

Its responsibility is:

"Get the raw data from the configured source and tell the next pipeline stage where the data is located.


You now have two classes.

S3Operation
Responsible for:

How do I communicate with S3?


DataIngestion
Responsible for:

How do I ingest data into my ML pipeline?

"""


class Data_Ingestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

        self.s3 = S3Operations()

    def get_data_from_s3(self)-> None:
        try:
                self.s3.sync_folder_from_S3(
                    folder = self.data_ingestion_config.data_path,
                    bucket_name = self.data_ingestion_config.bucket_name,
                    bucket_folder_name = self.data_ingestion_config.s3_data_folder
                )

        except Exception as e:
         raise XrayException(e, sys)



        

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:    ## "This method is expected to return a DataIngestionArtifacts object."

        try:
            self.get_data_from_s3()   ## do all the things mentioned in above mthd i.e get_data_from_s3()

            data_ingestion_artifacts: DataIngestionArtifacts = DataIngestionArtifacts(
                ## "The variable data_ingestion_artifact is expected to contain a DataIngestionArtifact object."

                train_data_filepath = self.data_ingestion_config.train_data_path,
                test_data_filepath = self.data_ingestion_config.test_data_path

            )   ## This is creating an object of the DataIngestionArtifact class.

            return data_ingestion_artifacts

        except Exception as e:
            raise XrayException(e, sys)
