from django.db import models

class Review(models.Model):
    review_body = models.TextField()
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    