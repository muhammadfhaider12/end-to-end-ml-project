import os
import sys
from src.ml_end_to_end.exception import CustomException
from src.ml_end_to_end.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
import os
from sqlalchemy import create_engine

load_dotenv(override=True)


host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")



def read_sql_data():
    logging.info("📦 Reading SQL database started")
    try:
        connection_string = f"mysql+pymysql://{user}:{password}@{host}/{db}"
        engine = create_engine(connection_string)
        logging.info("✅ SQLAlchemy engine created successfully")

        df = pd.read_sql_query("SELECT * FROM students", engine)
        logging.info("✅ DataFrame created from SQL query")
        print(df.head())
        return df
    

    except Exception as ex:
        raise CustomException(ex, sys)

# def read_sql_data():
#     logging.info("Reading SQL database started")
#     try:

#         connection_string = f"mysql+pymysql://{user}:{password}@{host}/{db}"
#         engine = create_engine(connection_string)
#         logging.info(f"Connection Establishment for {engine}")
#         df = pd.read_sql_query("SELECT * FROM students", engine)
#         return df

#     except Exception as ex:
#         raise CustomException(ex,sys)


# def read_sql_data():
#     logging.info("Reading SQL database started")
#     try:
#         mydb=pymysql.connect(
#             host=host,
#             user=user,
#             password=password,
#             db=db
#         )
        # logging.info(f"Connection Establishment for {mydb}")
        # df=pd.read_sql_query("Select * from students", mydb)

    #     return df

    # except Exception as ex:
    #     raise CustomException(ex,sys)