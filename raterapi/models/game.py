from django.db import models
from django.db.models.deletion import CASCADE
from .category import Category

class Game(models.Model):
    title = models.CharField(max_length=50)
    designer = models.CharField(max_length=50)
    description = models.CharField(max_length=160)
    year_released = models.IntegerField()
    num_players = models.IntegerField()
    game_image = models.ImageField(name='game_image', default="")
    category = models.ForeignKey("Category", on_delete=CASCADE, related_name="categories",
    related_query_name="category", default=1)
