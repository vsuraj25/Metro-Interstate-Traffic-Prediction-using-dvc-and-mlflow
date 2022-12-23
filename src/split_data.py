import pandas as pd
import sys
import argparse
from util.util import read_yaml
from exception import Project_Exception
from logger import logging
from sklearn.model_selection import train_test_split
# repro
def split_data(config_path):
    try:
        logging.info(f"{'-'*30} Spliting the model ready data into train and test files. {'-'*30}")
        logging.info('Reading Parameters.')
        config = read_yaml(config_path)

        model_data_path = config['prepare_data']['model_data_path']
        train_data_path = config['split_data']['train_path']
        test_data_path = config['split_data']['test_path']
        random_state = config['base']['random_state']
        test_size = config['split_data']['test_size']

        logging.info('Loading data as dataframe.')
        df = pd.read_csv(model_data_path, sep=',')

        logging.info(f'Creating train test split with test size = {test_size} and random state = {random_state}.')
        train, test = train_test_split(df, test_size=test_size, random_state=random_state)
        logging.info('Train test split created successfully.')

        logging.info(f'Saving train data as csv at {train_data_path} and test data as csv in {test_data_path} .')
        train.to_csv(train_data_path, sep = ',', index = False, encoding = 'utf-8')
        test.to_csv(test_data_path, sep= ',', index = False, encoding = 'utf-8')
        logging.info(f'Train and test data saved at {train_data_path} and {test_data_path} respectively.')

    except Exception as e:
        logging.error(Project_Exception(e, sys))
        raise Project_Exception(e, sys) from e


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    split_data(config_path = parsed_args.config)