from django.db import models

class College(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Position(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Team(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):

    playerID = models.AutoField(primary_key=True)
    playerNFLID = models.IntegerField()
    playerName = models.CharField(max_length=100)
    jerseyNumber = models.IntegerField()
    playerHeight = models.CharField(max_length=10)
    playerWeight = models.IntegerField()
    birthDate = models.CharField(max_length=50)
    season = models.IntegerField()

    playerCollege = models.ForeignKey(College, on_delete=models.DO_NOTHING)
    playerPosition = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    playerTeam = models.ForeignKey(Team, on_delete=models.DO_NOTHING)

    @property
    def get_team_name(self):
        return self.playerTeam.name
    @property
    def get_position(self):
        return self.playerPosition.name
    @property
    def get_college_name(self):
        return self.playerCollege.name

    def __str__(self):
        return self.playerName





