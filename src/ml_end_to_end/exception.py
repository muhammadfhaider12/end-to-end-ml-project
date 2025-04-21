import sys
from src.ml_end_to_end.logger import logging


def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()  # gets traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # file name
    line_number = exc_tb.tb_lineno              # line number
    error_message = f"Error occurred in file '{file_name}' at line {line_number}: {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)


    
    def __str__(self):
        return self.error_message