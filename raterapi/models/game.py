from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from .category import Category
from .game_rating import GameRating

class Game(models.Model):
    title = models.CharField(max_length=50)
    designer = models.CharField(max_length=50)
    description = models.CharField(max_length=160)
    year_released = models.IntegerField()
    num_players = models.IntegerField()
    game_image = models.ImageField(name='game_image', default="")
    category = models.ForeignKey("Category", on_delete=CASCADE, related_name="categories", related_query_name="category", default=1)

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = GameRating.objects.filter(game=self)

        # Sum of all of the ratings for the game
        total_rating = 0
        
        if len(ratings) == 0:
            return 0

        for rating in ratings:
            total_rating += rating.rating

        avg_rating = total_rating / len(ratings)
        return avg_rating
