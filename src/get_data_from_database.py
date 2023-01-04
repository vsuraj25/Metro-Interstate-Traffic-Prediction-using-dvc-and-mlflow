from pymongo import MongoClient
import pandas as pd
import argparse
import sys
from util.util import read_yaml
from logger import logging
from exception import Project_Exception
from dbconstant import connection_string,collection_name,database_name

def upload_get_data(param_config_path):
    try:
        logging.info(f"{'-'*30} Loading the data from database {'-'*30}")
        logging.info("Reading required parameters.")

        param_config = read_yaml(param_config_path)
        
        connection_str = connection_string
        database = database_name
        source_data_path = param_config['data_source']['source_data']
        table = collection_name

        logging.info("Connecting to MongoDB client.")
        client = MongoClient(connection_str)
        # Creating a Database with specified name
        logging.info("Getting Database.")
        db =  client.get_database(database)

        logging.info("Checking if updated records exists.")

        if table in db.list_collection_names():
            logging.info("Record already present.")
            records = db.get_collection(table)
            logging.info("Extracting data from database.")
            all_records = records.find()
            logging.info("Data Extracted Successfully.")
            # Converting Curser object into list
            cursor_list = list(all_records)

            logging.info("Converting data into dataframe.")
            data = pd.DataFrame(cursor_list).drop('_id', axis=1)
            logging.info("Dataframe ready.")

            return data

        else:
            logging.info("No Records present.")
            logging.info("Loading the source data into database.")
            records = db.traffic_records

            df = pd.read_csv(source_data_path)

            # Converting the dataframe into sictionary as MongoDB stores values as records/dictionary
            df = df.to_dict(orient='records')

            # Inserting the records into our mongoDB Database in collection 'fire_records'
            records.insert_many(df)
            logging.info("Data inserted into the database successfully.")

            logging.info("Extracting data from database.")
            all_records = records.find()
            logging.info("Data Extracted Successfully.")
            # Converting Curser object into list
            cursor_list = list(all_records)

            logging.info("Converting data into dataframe.")
            data = pd.DataFrame(cursor_list).drop('_id', axis=1)
            logging.info("Dataframe Ready.")

            return data
    except Exception as e:
        logging.error(Project_Exception(e, sys))
        raise Project_Exception(e, sys) from e

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    data = upload_get_data(param_config_path=parsed_args.config)