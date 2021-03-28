from django.apps import AppConfig
import pandas as pd
from joblib import load
import os

class PredictionConfig(AppConfig):
    name = 'prediction'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MLMODEL_FOLDER = os.path.join(BASE_DIR, 'prediction/')
    MLMODEL_FILE = os.path.join(MLMODEL_FOLDER, "NFLPrediction.joblib")
    mlmodel = load(MLMODEL_FILE)
    