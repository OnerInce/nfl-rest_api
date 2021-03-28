from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.NFL_Model_Predict.as_view(), name="api_predict")
]