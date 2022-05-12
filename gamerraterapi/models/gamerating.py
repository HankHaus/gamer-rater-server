from django.db import models

class GameRating(models.Model):
    rating = models.CharField(max_length=15)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    