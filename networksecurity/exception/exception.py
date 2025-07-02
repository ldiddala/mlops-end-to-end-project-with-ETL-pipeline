import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: str, error_details: sys):
        self.error_message = error_message
        _,_, exc_info = error_details.exc_info()

        self.line_number = exc_info.tb_lineno
        self.file_name = exc_info.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in the file {self.file_name} at line number {self.line_number}: Error message: {self.error_message}"

if __name__ == "__main__":

    try:
        logger.logging.info("Enter try block")
        div = 1/0
        print("After the error")

    except Exception as e:
        raise NetworkSecurityException(e, sys)