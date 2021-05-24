from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Player, Team
from .serializers import PlayerSerializer, TeamSerializer


def APIWelcomeView(request):

    return JsonResponse({'result':'error', 'message':'Use with /api/teams or /api/players'}, status=404)

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