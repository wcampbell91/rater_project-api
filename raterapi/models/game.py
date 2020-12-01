from django.db import models
from django.db.models.deletion import CASCADE
from .category import Category

class Game(models.Model):
    title = models.CharField(max_length=50)
    designer = models.CharField(max_length=50)
    description = models.CharField(max_length=160)
    year_released = models.IntegerField()
    num_players = models.IntegerField()
    game_image = models.ImageField(verbose_name='game_image', name='game_image', width_field='300',height_field='300', default="")
# REMIGRATE!
