import pandas as pd
import argparse
import sys
from util.util import read_yaml
from get_data_from_database import upload_get_data
from logger import logging
from exception import Project_Exception
# repro
def load_data(config_path):
    try:
        config = read_yaml(config_path)
        df = upload_get_data(config_path)
        raw_data_path = config['load_data']['raw_dataset_csv']

        logging.info(f'Saving the data as csv at {raw_data_path}')
        df.to_csv(raw_data_path, sep=',', index= False)
        logging.info(f'Data saved at {raw_data_path}')
    except Exception as e:
        logging.error(Project_Exception(e, sys))
        raise Project_Exception(e,sys) from e


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    load_data(config_path = parsed_args.config)
    