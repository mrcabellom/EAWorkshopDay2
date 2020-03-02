import json
import pickle
import os
import numpy as np
import logging
from joblib import load
from azureml.core.model import Model


def init():
    global model
    model_path = Model.get_model_path('RandomForestregressor')
    model = load(model_path)
   
def run(raw_data):

    input_data = np.array([json.loads(raw_data)['data']])
    output = model.predict(input_data)
    return {"inference": output.tolist()}