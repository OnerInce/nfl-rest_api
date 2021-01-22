from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Player, Team
from .serializers import PlayerSerializer, TeamSerializer


class PlayerView(viewsets.ReadOnlyModelViewSet):

    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    def get_queryset(self):
        queryset = Player.objects.all()

        if len(self.request.query_params) > 0:
            season = self.request.query_params.get('season')
            team = self.request.query_params.get('team').upper()
            team_idd = Team.objects.get(name=team).id
            queryset = queryset.filter(season=season, playerTeam=team_idd)

        return queryset


class TeamView(viewsets.ReadOnlyModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer