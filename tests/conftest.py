import pytest
import yaml
import os
import json
import logging
import joblib
from prediction_service.prediction import form_response, api_response



@pytest.fixture
def config(config_path = 'params.yaml'):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

@pytest.fixture
def schema_in(schema_path = 'schema_in.json'):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema