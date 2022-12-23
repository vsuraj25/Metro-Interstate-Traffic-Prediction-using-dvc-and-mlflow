import pandas as pd
import numpy as np
import argparse
from logger import logging
from exception import DataNotValid
from exception import Project_Exception
from logger import logging
from util.util import read_yaml
import sys
# repro
def validate_data(config_path):
    try:
        logging.info(f"{'-'*30} Validating the dataset {'-'*30}")
        config = read_yaml(config_path)
        logging.info("Reding validation schema.")
        schema = config['validate_data']['schema']
        schema_columns = schema['columns']
        schema_total_cols = schema['no_of_cols']
        schema_total_rows = schema['no_of_rows']
        data_path = config['load_data']['raw_dataset_csv']
        logging.info("Loading the data.")
        df = pd.read_csv(data_path)
        
        val_cols = validate_columns(schema_columns, df)
        val_total_cols = validate_no_of_cols(schema_total_cols,df)
        val_total_rows = validate_no_of_rows(schema_total_rows, df)
        validation_status = val_cols and val_total_cols and val_total_rows

        if validation_status:
            pass
        else:
            raise DataNotValid
    except Exception as e:
        logging.error(Project_Exception(e, sys))
        raise Project_Exception(e, sys) from e


def validate_columns(schema, df):
    logging.info("Validating columns.")
    validation_status = False
    for i in df.columns:
        if i not in list(schema.keys()):
            validation_status = False
            logging.info(f"Invalid columns found - {i}.")
            break
        else:
            validation_status = True
        
        if df[i].dtype != schema[i]:
            validation_status = False
            logging.info(f"Invalid data type found - {i} : {df[i].dtype}.")
            break
        else:
            validation_status = True

    if validation_status:
        logging.info("All Columns are valid.")
    else:
        logging.info("Failed to validate columns.")

    return validation_status

def validate_no_of_cols(schema_no_of_cols, df):
    logging.info("Validating number of columns.")
    validation_status = False

    if schema_no_of_cols == df.shape[1]:
        validation_status = True
        logging.info("Valid number of columns found.")
    else:
        validation_status = False
        logging.info(f"Invalid no of columns - {df.shape[1]}.")
        logging.info("Failed to validate total number of columns.")
        
    return validation_status

def validate_no_of_rows(schema_no_of_rows, df):
    logging.info("Validating number of rows.")
    validation_status = False
    
    if schema_no_of_rows == df.shape[0]:
        validation_status = True
        logging.info("Valid number of rows found.")
    else:
        validation_status = False
        logging.info(f"Invalid no of rows - {df.shape[0]}.")
        logging.info("Failed to validate total number of rows.")
    
    return validation_status


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    validate_data(parsed_args.config)
