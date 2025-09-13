import sys
import logging
from src.logger import logging
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script [{0}] at line [{1}] with error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__=="__main__":
    try:
        a=1/0
    except Exception as a:
        logging.info("Divide by Zero")
        raise CustomException(a,sys)