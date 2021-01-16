from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

class GameReview(models.Model):
    review = models.CharField(max_length=250)
    game = models.ForeignKey("Game", on_delete=CASCADE, related_name="reviews", related_query_name="review")
    player = models.ForeignKey("Player", on_delete=CASCADE, related_name="players", related_query_name="player")
