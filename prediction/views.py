from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from prediction.apps import PredictionConfig, sample_json_dict
from django.http import JsonResponse
from players.models import Rusher_Avg
import pandas as pd
import numpy as np


def get_rusher_avgs(rusher_nfl_id):
    rusher_row = Rusher_Avg.objects.filter(nfl_id=rusher_nfl_id).values_list('avg_speed', 'avg_acc')
    speed, acc = list(rusher_row)[0][0], list(rusher_row)[0][1]

    return speed, acc

def predict_game_weather(temp_input, wind_speed_input):
    loaded_model = PredictionConfig.weather_model
    y_pred = loaded_model.predict(np.array([temp_input, wind_speed_input]).reshape(1, -1))
    return y_pred[0]

class NFL_Model_Predict(APIView):
    def post(self, request, format=None):
        data = request.data
        if len(data) < 1:
            return JsonResponse({'result':'error', 'message':'No parameters given'}, status=404)

        values = []
        rusher_id, temperature, wind_speed = -1, -1, -1

        for key in sample_json_dict:
            if key == "Temperature":
                temperature = data[key]
                continue
            elif key == "WindSpeed":
                wind_speed = data[key]
                predicted_weather = predict_game_weather(temperature, wind_speed)
                values.append(predicted_weather)
                continue
            elif key == "rusher_NflId":
                rusher_id = data[key]
                speed, acc = get_rusher_avgs(rusher_id)
            values.append(data[key])

        values.append(speed)
        values.append(acc)

        X = pd.Series(values).to_numpy().reshape(1, -1)
        loaded_model = PredictionConfig.ml_model
        y_pred = loaded_model.predict(X)
        y_pred = pd.Series(y_pred)
        
        response_dict = {"prediction": y_pred[0]}
        return Response(response_dict, status=200)