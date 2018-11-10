from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import pytz

utc=pytz.UTC


# Create your models here.


class GameType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    rules = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    #user = models.OneToOneField(User, blank=True, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    nick_name = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    last_game_date = models.DateTimeField(blank=True, null=True)
    last_game_id = models.IntegerField(blank=True, null=True)
    ninety_day_games_played = models.FloatField(default=2)
    ninety_day_plus_minus = models.FloatField(default=2)
    win_contribution = models.FloatField(default=0)
    score_contribution = models.FloatField(default=0)
    ninety_day_win_percentage = models.FloatField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        if self.nick_name:
            return self.first_name + " " + str(self.last_name) + " (" + self.nick_name + ")"
        else:
            return self.first_name + " " + str(self.last_name)

class Game(models.Model):
    game_type = models.ForeignKey(GameType, on_delete=models.DO_NOTHING)
    player_1 = models.ForeignKey(Player, related_name = 'player_1', on_delete=models.DO_NOTHING)
    player_2 = models.ForeignKey(Player, related_name = 'player_2', on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    notes = models.CharField(max_length=2000, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def game_duration_friendly(self):

        if self.end_time == None:
            game_end = datetime.now()
        else:
            game_end = self.end_time

        return utc.localize(game_end) - self.start_time


    def __str__(self):
        return "%s: %s (%s)"  % (self.name, self.start_time, self.game_duration_friendly)


    



