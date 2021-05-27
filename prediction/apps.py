from django.apps import AppConfig
from joblib import load
import os
import json

class PredictionConfig(AppConfig):
    name = 'prediction'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MLMODEL_FOLDER = os.path.join(BASE_DIR, 'prediction/')
    MLMODEL_FILE = os.path.join(MLMODEL_FOLDER, "main_model.joblib")
    ml_model = load(MLMODEL_FILE)
    sample_json_dict = {}

    WHEATHER_MODEL_FILE = os.path.join(MLMODEL_FOLDER, "weather_model.joblib")
    weather_model = load(WHEATHER_MODEL_FILE)

    with open('sample.json') as f:
        sample_json_dict = json.load(f)

