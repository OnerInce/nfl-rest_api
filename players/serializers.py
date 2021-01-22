from rest_framework import serializers
from .models import Player, Team

class PlayerSerializer(serializers.ModelSerializer):

    playerTeam = serializers.ReadOnlyField(source="get_team_name")
    playerPosition = serializers.ReadOnlyField(source="get_position")
    playerCollege = serializers.ReadOnlyField(source="get_college_name")

    class Meta:
        model = Player
        #fields = '__all__'
        fields = ("playerID", "playerNFLID", "playerName", "season", "jerseyNumber", "playerHeight", "playerWeight", "birthDate", "playerCollege", "playerPosition", "playerTeam")

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'
        fields = ['id', 'name']