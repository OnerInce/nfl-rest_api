from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Player, Team
from .serializers import PlayerSerializer, TeamSerializer

def WelcomeView(request):

    message = "<body>Welcome to the Nfl Rest API. Use API with /api</body>"

    return HttpResponse(message)


def APIWelcomeView(request):

    message = "<body>Use with /teams or /players</body>"

    return HttpResponse(message)


class PlayerView(viewsets.ReadOnlyModelViewSet):

    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    def get_queryset(self):
        queryset = Player.objects.all()

        if len(self.request.query_params) > 0:
            season = self.request.query_params.get('season')
            team = self.request.query_params.get('team').upper()
            team_idd = Team.objects.get(name=team).id
            queryset = queryset.filter(season=season, team_name=team_idd)

        return queryset


class TeamView(viewsets.ReadOnlyModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer