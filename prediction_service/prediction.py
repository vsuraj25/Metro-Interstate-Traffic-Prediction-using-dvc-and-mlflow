import yaml
import json
import joblib
import numpy as np

param_path = 'params.yaml'

def read_yaml(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def form_response(dict_req):
    data = dict_req.values()
    data = [list(map(float, data))]
    response = predict(data)
    return response

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {'response' : response}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Something went wrong!! Try again"}
        return error

def predict(data):
    config = read_yaml(param_path)
    prediction_model = config['web_model_dir']
    model = joblib.load(prediction_model)
    prediction = model.predict(data).tolist()[0]

    return prediction


    
