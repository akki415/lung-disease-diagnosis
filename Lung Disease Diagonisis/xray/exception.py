# HERE WE WILL CREATE A FILE NECESSARY FOR ERROR HANDLING AND BACKTRACK

"""
WHEN AN ERROR HAPPENS:

    1. Get the original error
    2. Find which Python file caused it
    3. Find which line caused it
    4. Combine all three pieces of information
    5. Create a custom exception
    6. Display the detailed message

"""

import os
import sys   # sys provides access to Python's runtime/system information, i.e information about the currently handled exception


def error_message_details(error:Exception, error_details:sys) -> str:
    _,_,exc_tb = error_details.exc_info()                       # what will the exception information will contain 


    file_name:str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]   # backtrack -> find the frame where error -> frame to code -> code to file

    error_message:str = "Error occured @ python script name [{0}]  @ line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message



class XrayException(Exception):
    #XrayException is based on Python's built-in Exception class.
    #So XrayException gets the normal behavior of an exception, and you are adding your own behavior to it.
    # Exception is the parent class & XrayException is the child class.


    def __init__(self, error_message, error_details):
        # __init__ is a special method that runs automatically when you create an object.
        # when you call this class, init mthd automatically runs without even manually calling
        """
        except Exception as error:
        raise XrayException(error, sys)
        """
        # here when you call XrayException class which creates an XrayException obj.
        # in which the params provided by init as it automatically executed on calling of class



        super().__init__(error_message)
        # super() --> "I want to access functionality from my parent class."

        self.error_message = error_message_details(error_message, error_details=error_details)

    def __str__(self):
            return self.error_message