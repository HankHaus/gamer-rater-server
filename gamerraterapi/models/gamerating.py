from django.db import models

class GameRating(models.Model):
    rating = models.CharField(max_length=15)
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    