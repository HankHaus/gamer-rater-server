from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_in_minutes = models.IntegerField()
    age_recommendation = models.CharField(max_length=20)
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    