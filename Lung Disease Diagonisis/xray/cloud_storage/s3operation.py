import os
import sys # system module

from xray.exception import XrayException


class S3Operations:


    def sync_folder_to_S3(self, 
                        folder:str, 
                        bucket_name:str, 
                        bucket_foler_name:str) -> None:
        try:
            command:str =(f"aws S3 sync {folder} S3://{bucket_name}/{bucket_foler_name}/"    ## Synchronize the contents of /app/data{folder} with the S3 location s3://my-bucket/backup/.
            )

            os.system(command)    ## os.system() asks the operating system to execute the string as a shell command

        except Exception as e:
            raise XrayException(e, sys)



    def sync_folder_from_S3(self,
                            folder:str,
                            bucker_name:str,
                            bucket_folder_name:str) -> None: 
        try:
            command:str = ( f"aws S3 sync S3://{bucker_name}/{bucket_folder_name} / {folder} "

            )

            os.system(command)

        except Exception as e:
            raise XrayException(e, sys)





"""
             Python Application
                    │
                    │ calls
                    ▼
              S3Operation
               /        \
              /          \
             ▼            ▼
    sync_folder_to_s3   sync_folder_from_s3
             │            │
             └─────┬──────┘
                   │
                   ▼
             os.system()
                   │
                   ▼
              AWS CLI
                   │
                   ▼
             Amazon S3
"""        




        