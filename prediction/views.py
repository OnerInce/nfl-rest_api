from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from prediction.apps import PredictionConfig
from django.http import HttpResponse

class NFL_Model_Predict(APIView):
    def post(self, request, format=None):
        data =  request.data
        keys, values = [], []

        for key in data:
            keys.append(key)
            values.append(data[key])

        X = pd.Series(values).to_numpy().reshape(1, -1)
        loaded_model = PredictionConfig.mlmodel
        y_pred = loaded_model.predict(X)
        y_pred = pd.Series(y_pred)
        
        response_dict = {"Predicted Yard Gain ": y_pred[0]}
        return Response(response_dict, status=200)