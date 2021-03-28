"""nflapi URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from .views import WelcomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeView),
    path('api/', include('players.urls')),
    path('predict/', include('prediction.urls')),
]
