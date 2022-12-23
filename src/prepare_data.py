import pandas as pd
import numpy as np
from logger import logging
from exception import Project_Exception
import argparse
import sys
from util.util import read_yaml
from sklearn.preprocessing  import LabelEncoder
# repro
def prepare_data(config_path):
    try:
        logging.info(f"{'-'*30} Preparing the data {'-'*30}")
        logging.info("Reading Parameters.")
        config = read_yaml(config_path)

        data_path = config['load_data']['raw_dataset_csv']
        clean_data_path = config['prepare_data']['cleaned_data_path']
        model_data_path = config['prepare_data']['model_data_path']

        logging.info("Loading the validated data.")
        df = pd.read_csv(data_path)
        logging.info("Data loaded as a pandas dataframe.")

        logging.info("Dropping columns that are not required - snow_1h', 'rain_1h', 'weather_description.")
        new_df = df.drop(['snow_1h', 'rain_1h', 'weather_description'], axis = 1)

        logging.info("Dropping 0's values from temperature.")
        new_df = new_df.drop(new_df[new_df['temp']==0].index, axis = 0)

        logging.info("Parsing all holidays into a single unit 'holiday'.")
        def parse_holiday(holiday):
            val = 'None' 
            if holiday != 'None':
                val = 'holiday'
            return val

        new_df['holiday'] = new_df['holiday'].map(parse_holiday)

        logging.info("Removing Duplicate Values.")
        new_df.drop_duplicates(inplace=True)

        logging.info("Parsing date_time feature to pd.DateTime.")
        new_df['date_time'] = pd.to_datetime(new_df['date_time'])

        logging.info("Creating new columns from datetime column - year, month, weekday, hour.")
        new_df['year'] = new_df['date_time'].dt.year
        new_df['month'] = new_df['date_time'].dt.month
        new_df['weekday'] = new_df['date_time'].dt.weekday
        new_df['hour'] = new_df['date_time'].dt.hour

        logging.info("Creating a new column for categorizing hours into parts of a day.")
        def categorize_hour(hour):
            cat = None
            if hour in [1,2,3,4,5]:
                cat = 'dawn'
            elif hour in [6,7,8,9,10,11,12]:
                cat = 'morning'
            elif hour in [13,14,15,16,17,18]:
                cat = 'afternoon'
            elif hour in [19,20,21,22,23,0]:
                cat = 'night'

            return cat

        new_df['day_part'] = new_df['hour'].map(categorize_hour)

        logging.info("Data Cleaning and Feature Engineering Completed.")

        logging.info(f"Saving the cleaned data at {clean_data_path}.")
        new_df.to_csv(clean_data_path, header = True, index=False)

        logging.info("Preparing model data with selected features.")
        logging.info("Dropping columns that are not required for model training - 'day_part', 'date_time', 'year' .")
        model_df = new_df.drop(['day_part', 'date_time', 'year'], axis = 1)

        logging.info("Label Encoding Categorical Features.")
        le = LabelEncoder()
        for column in model_df.columns:
            if model_df[column].dtypes == 'object':
                model_df[column] = le.fit_transform(model_df[column])

        logging.info(f"Saving model ready data at {model_data_path}.")
        model_df.to_csv(model_data_path, header=True, index = False)

    except Exception as e:
        logging.error(Project_Exception(e, sys))
        raise Project_Exception(e, sys) from e


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    prepare_data(config_path = parsed_args.config)