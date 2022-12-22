import pytest
import logging
import os
import joblib
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "correct_range":
    {
    "holiday":0.0,
    "temp":289.36,
    "clouds_all":75.0,
    "weather_main":1.0,
    "month":10.0,
    "weekday":1.0,
    "hour":10.0
    },

    "incorrect_range":
    {
    "holiday":0,
    "temp":122.36,
    "clouds_all":75.0,
    "weather_main":13,
    "month":13,
    "weekday":9,
    "hour":10.0
    },

    "incorrect_cols":
    {
    "holiday":0.0,
    "temp":289.36,
    "clouds all":75.0,
    "weather main":1.0,
    "month":10.0,
    "weekdays":1.0,
    "hour":10.0
    }
}

Target_range = {
        "min":0.0,
        "max":7280.0
    }

def test_form_response_correct_range(data = input_data["correct_range"]):
    res = form_response(data)
    assert Target_range["min"]<= res <= Target_range["max"] 

def test_api_response_correct_range(data = input_data["correct_range"]):
    res = api_response(data)
    assert Target_range["min"]<= res['response'] <= Target_range["max"] 

def test_from_response_incorrect_range(data = input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data = input_data["incorrect_range"]):
    res = api_response(data)
    assert res['response'] == prediction_service.prediction.NotInRange().message

def test_api_response_incorrect_cols(data = input_data["incorrect_cols"]):
    res = api_response(data)
    assert res['response'] == prediction_service.prediction.NotInCol().message