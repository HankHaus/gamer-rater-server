from django.db import models

class Review(models.Model):
    review_body = models.TextField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    