import pandas as pd
import argparse
import sys
from logger import logging
from exception import Project_Exception
from util.util import read_yaml


def train_and_evaluate(config_path):
    try:
        config = read_yaml(config_path)
        train_data_path = config['split_data']['train_path']
        test_data_path = config['split_data']['test_path']
        
    except Exception as e:
        raise Project_Exception(e, sys) from e


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    train_and_evaluate(config_path= parsed_args.config)