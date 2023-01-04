import pandas as pd
import argparse
import sys
import numpy as np
import os
import joblib
import json
import mlflow
from urllib.parse import urlparse
from logger import logging
from exception import Project_Exception
from util.util import read_yaml
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor


def train_and_evaluate(config_path):
    try:
        logging.info(f"{'-'*30} Training and evaluating the model with mlflow. {'-'*30}")
        logging.info('Spliting the model ready data into train and test files.')
        logging.info('Reading Parameters.')
        config = read_yaml(config_path)
        train_data_path = config['split_data']['train_path']
        test_data_path = config['split_data']['test_path']

        alpha = config['train_evaluate']['estimators']['XGBoostRegressor']['params']['alpha']
        cosample_bytree = config['train_evaluate']['estimators']['XGBoostRegressor']['params']['cosample_bytree']
        max_depth = config['train_evaluate']['estimators']['XGBoostRegressor']['params']['max_depth']
        min_child_weight = config['train_evaluate']['estimators']['XGBoostRegressor']['params']['min_child_weight']
        subsample = config['train_evaluate']['estimators']['XGBoostRegressor']['params']['subsample']
        
        prediction_model_path = config['train_evaluate']['prediction_model_path']
        score_file_path = config['train_evaluate']['reports']['scores_file']
        params_file_path = config['train_evaluate']['reports']['params_file']

        target = config['base']['target_col']

        logging.info('Reading test and train data.')
        train_data = pd.read_csv(train_data_path, sep=',')
        test_data = pd.read_csv(test_data_path, sep=',')

        logging.info('Splitting x_train, y_train, x_test and y_test.')
        x_train = train_data.drop(target, axis=1).values
        x_test = test_data.drop(target, axis=1).values

        y_train = train_data[target]
        y_test = test_data[target]

        mlflow_config = config['mlflow_config']
        remote_server_uri = mlflow_config['remote_server_uri']

        logging.info('Setting up mlflow tracking uri.')
        mlflow.set_tracking_uri(remote_server_uri)

        logging.info('Setting up mlflow experiment as {}.'.format(mlflow_config['experiment_name']))
        mlflow.set_experiment(mlflow_config['experiment_name'])

        logging.info('Starting mlflow run as {}.'.format(mlflow_config['run_name']))
        with mlflow.start_run(run_name = mlflow_config['run_name']) as mlops_run:

            logging.info(f'Using best model - XGBRegressor for model training with parameters alpha : \
                        {alpha}, cosample_bytree : {cosample_bytree}, max_depth : {max_depth}, min_child_weight: \
                            {min_child_weight}, subsample: {subsample}.')
            xgb = XGBRegressor(
                alpha = alpha,
                cosample_bytree = cosample_bytree,
                max_depth = max_depth,
                min_child_weight = min_child_weight,
                subsample = subsample
            )
            logging.info('Fitting scaled x_train and y_train.')
            xgb.fit(x_train, y_train)

            logging.info('Predicting on test data.')
            y_pred = xgb.predict(x_test)

            logging.info('Evalauting Metrics.')
            rmse, mae, r2 = evaluate_metrics(y_test, y_pred)

            logging.info('Logging all parameters in mlflow.')
            mlflow.log_param('alpha', alpha)
            mlflow.log_param('cosample_bytree', cosample_bytree)
            mlflow.log_param('max_depth', max_depth)
            mlflow.log_param('min_child_weight', min_child_weight)
            mlflow.log_param('subsample', subsample)

            logging.info('Logging all metrics in mlflow.')
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            tracking_url_type_store = urlparse(mlflow.get_artifact_uri()).scheme

            if tracking_url_type_store != 'file':
                mlflow.sklearn.log_model(xgb, "model", registered_model_name = mlflow_config['registered_model_name'])
            else:
                mlflow.sklearn.load_model(xgb, "model")

            scores = {'rmse': rmse, 'mae': mae, 'r2' : r2}
            params = {'alpha' : alpha, 'cosample_bytree' : cosample_bytree, 'max_depth' : max_depth, 'min_child_weight': \
                    min_child_weight, 'subsample': subsample}
            
            logging.info(type(xgb).__name__)
            logging.info(f'Parametes : {params}')
            logging.info(f"Scores : {scores}")

            logging.info(f'Saving scores and parameters report at {score_file_path} and {params_file_path} respectively.')
            with open(score_file_path, 'w') as f:
                json.dump(scores, f, indent=4)

            with open(params_file_path, 'w') as f:
                json.dump(params, f, indent=4)

            logging.info('Model Reports saved.')

            logging.info(f'Saving model at {prediction_model_path}')
            os.makedirs(prediction_model_path, exist_ok=True)
            model_path = os.path.join(prediction_model_path, 'model.joblib')
            joblib.dump(xgb, model_path)
            logging.info(f'Model Saved at {prediction_model_path}.')

    except Exception as e:
        logging.error(Project_Exception(e, sys))
        raise Project_Exception(e, sys) from e

def evaluate_metrics(actual, pred):
    mse = mean_squared_error(actual, pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)

    return rmse, mae, r2


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    train_and_evaluate(config_path= parsed_args.config)