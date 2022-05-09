from django.db import models

class Picture(models.Model):
    url = models.TextField()
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    