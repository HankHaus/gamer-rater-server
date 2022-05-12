from django.db import models

class Picture(models.Model):
    url = models.TextField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    