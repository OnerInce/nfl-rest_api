from rest_framework import serializers
from .models import Player, Team

class PlayerSerializer(serializers.ModelSerializer):

    playerID = serializers.ReadOnlyField(source="id")
    playerNFLID = serializers.ReadOnlyField(source="nfl_id")
    playerName = serializers.ReadOnlyField(source="display_name")
    jerseyNumber = serializers.ReadOnlyField(source="jersey_number")
    playerHeight = serializers.ReadOnlyField(source="height")
    playerWeight = serializers.ReadOnlyField(source="weight")
    birthDate = serializers.ReadOnlyField(source="birth_date")
    isOffense = serializers.ReadOnlyField(source="is_offense")

    playerTeam = serializers.PrimaryKeyRelatedField(source="get_team_name", read_only=True)
    playerPosition = serializers.PrimaryKeyRelatedField(source="get_position", read_only=True)
    playerCollege = serializers.PrimaryKeyRelatedField(source="get_college_name", read_only=True)

    class Meta:
        model = Player
        fields = ("playerID", "playerNFLID", "playerName", "season", "jerseyNumber", "playerHeight", "playerWeight", "birthDate", "playerCollege", "playerPosition", 'playerTeam', 
        "isOffense")

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'
        fields = ['id', 'name']