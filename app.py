from src.ml_end_to_end.logger import logging
from src.ml_end_to_end.exception import CustomException
from src.ml_end_to_end.components.data_injestion import DataIngestion
import sys


if __name__== "__main__":
    logging.info("The execution has started")
    
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_injestion()
        

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

 