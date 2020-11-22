from django.db import models
from django.db.models.deletion import CASCADE
from .category import Category

class Game(models.Model):
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    description = models.CharField(max_length=160)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    num_players = models.IntegerField()
    game_image = models.ImageField(verbose_name='game_img', name='img1', width_field='300',height_field='300')
    categories = models.ManyToManyField(Category)
