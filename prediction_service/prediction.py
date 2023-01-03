import yaml
import json
import os 
import joblib
import numpy as np


param_path = 'params.yaml'
schema_path = os.path.join('prediction_service', 'schema_in.json')


# Exception classes

class NotInRange(Exception):
    def __init__(self, message = 'Values entered are not in range!'):
        self.message = message
        super().__init__(self.message)

class NotInCol(Exception):
    def __init__(self, message = 'Invalid columns!'):
        self.message = message
        super().__init__(self.message)


def read_yaml(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_schema(schema_path = schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema

def validate_input(dict_request):

    def _validate_cols(col):
        schema = get_schema()
        actual_cols = schema.keys()
        if col not in actual_cols:
            raise NotInCol

    def _validate_values(col, val):
        schema = get_schema()
        if not (schema[col]['min'] <= float(dict_request[col]) <= schema[col]['max']):
            raise NotInRange

    for col, val in dict_request.items():
        _validate_cols(col)
        _validate_values(col, val)

    return True

def form_response(dict_request):
    if validate_input(dict_request):
        data = dict_request.values()
        data = [list(map(float, data))]
        response = predict(data)
        return response

def api_response(dict_request):
    try:
        dict_request = dict(dict_request)
        if validate_input(dict_request):
            data = np.array([list(dict_request.values())])
            response = predict(data)
            response = {'response' : response}
            return response

    except NotInRange as e:
        print(e)
        response = {'the_expected_range': get_schema(), 'response': str(e)}
        return response

    except NotInCol as e:
        print(e)
        response = {'the_expected_columns': list(get_schema().keys()), 'response': str(e)}
        return response

    except Exception as e:
        print(e)
        response = {'the_expected_range': get_schema(), 'response': str(e)}
        return response

def predict(data):
    config = read_yaml(param_path)
    prediction_model = config['web_model_dir']
    model = joblib.load(prediction_model)
    prediction = model.predict(data).tolist()[0]

    try:
        if 0 <= prediction <= 7280: 
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected Result"




    
