from django.db import models
from django.db.models.deletion import CASCADE

class GameReview(models.Model):
    review = models.CharField(max_length=250)
    game = models.ForeignKey("Game", on_delete=CASCADE)
    player = models.ForeignKey("Player", on_delete=CASCADE)
