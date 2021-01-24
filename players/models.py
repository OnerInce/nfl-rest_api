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

    id = models.AutoField(primary_key=True)
    nfl_id = models.IntegerField()
    display_name = models.CharField(max_length=100)
    jersey_number = models.IntegerField()
    height = models.CharField(max_length=10)
    weight = models.IntegerField()
    birth_date = models.CharField(max_length=50)
    season = models.IntegerField()
    is_offense = models.IntegerField()

    college_name = models.ForeignKey(College, on_delete=models.DO_NOTHING)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    team_name = models.ForeignKey(Team, on_delete=models.DO_NOTHING)

    @property
    def get_team_name(self):
        return self.team_name.name
    @property
    def get_position(self):
        return self.position.name
    @property
    def get_college_name(self):
        return self.college_name.name

    def __str__(self):
        return self.display_name





