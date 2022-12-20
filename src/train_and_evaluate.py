import pandas as pd
import argparse
import sys
import numpy as np
import os
import joblib
import json
from logger import logging
from exception import Project_Exception
from util.util import read_yaml
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor


def train_and_evaluate(config_path):
    try:
        logging.info(f"{'-'*30} Spliting the model ready data into train and test files. {'-'*30}")
        logging.info('Reading Parameters.')
        config = read_yaml(config_path)
        train_data_path = config['split_data']['train_path']
        test_data_path = config['split_data']['test_path']
        min_samples_split = config['train_evaluate']['estimators']['XGBoostRegressor']['params']['min_samples_split']
        min_samples_leaf = config['train_evaluate']['estimators']['XGBoostRegressor']['params']['min_samples_leaf']
        max_depth = config['train_evaluate']['estimators']['XGBoostRegressor']['params']['max_depth']
        save_best_model_path = config['train_evaluate']['save_model_path']
        score_file_path = config['train_evaluate']['reports']['scores_file']
        params_file_path = config['train_evaluate']['reports']['params_file']

        target = config['base']['target_col']

        logging.info('Reading test and train data.')
        train_data = pd.read_csv(train_data_path, sep=',')
        test_data = pd.read_csv(test_data_path, sep=',')

        logging.info('Splitting x_train, y_train, x_test and y_test.')
        x_train = train_data.drop(target, axis=1)
        x_test = test_data.drop(target, axis=1)

        y_train = train_data[target]
        y_test = test_data[target]

        logging.info('Scaling the independent features.')
        x_train_scaled, x_test_scaled = standard_scale(x_train, x_test)

        logging.info(f'Using best model - XGBRegressor for model training with parameters min_samples_leaf : \
                    {min_samples_leaf}, min_samples_split : {min_samples_split}, max_depth : {max_depth}.')
        xgb = XGBRegressor(
            min_samples_leaf = min_samples_leaf,
            min_samples_split = min_samples_split,
            max_depth = max_depth
        )
        logging.info('Fitting scaled x_train and y_train.')
        xgb.fit(x_train_scaled, y_train)

        logging.info('Predicting on test data.')
        y_pred = xgb.predict(x_test_scaled)

        logging.info('Evalauting Metrics.')
        rmse, mae, r2 = evaluate_metrics(y_test, y_pred)

        scores = {'rmse': rmse, 'mae': mae, 'r2' : r2}
        params = {'min_samples_leaf': min_samples_leaf, 'min_samples_split': min_samples_split, 'max_depth' : max_depth}
        
        logging.info(type(xgb).__name__)
        logging.info(f'Parametes : {params}')
        logging.info(f"Scores : {scores}")

        logging.info(f'Saving scores and parameters report at {score_file_path} and {params_file_path} respectively.')
        with open(score_file_path, 'w') as f:
            json.dump(scores, f, indent=4)

        with open(params_file_path, 'w') as f:
            json.dump(params, f, indent=4)

        logging.info('Model Reports saved.')

        logging.info(f'Saving model at {save_best_model_path}')
        os.makedirs(save_best_model_path, exist_ok=True)
        model_path = os.path.join(save_best_model_path, 'model.joblib')
        joblib.dump(xgb, model_path)
        logging.info(f'Model Saved at {save_best_model_path}.')

    except Exception as e:
        logging.error(Project_Exception(e, sys))
        raise Project_Exception(e, sys) from e

def evaluate_metrics(actual, pred):
    mse = mean_squared_error(actual, pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)

    return rmse, mae, r2


def standard_scale(x_train, x_test):
    scale = StandardScaler()
    x_train_scaled = scale.fit_transform(x_train)
    x_test_scaled = scale.transform(x_test)
    return x_train_scaled, x_test_scaled

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    train_and_evaluate(config_path= parsed_args.config)