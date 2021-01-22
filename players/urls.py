from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'players',  views.PlayerView, basename='players')
router.register(r'teams',  views.TeamView, basename='teams')

urlpatterns = [
    path('', views.WelcomeView),
    path('api', views.APIWelcomeView),
    path('api/', include((router.urls, 'app_name'))),
]