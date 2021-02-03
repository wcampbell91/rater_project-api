import json
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from raterapi.models import Game, GameRating, Player, Category

class GameRatingTests(APITestCase):
    def setUp(self):
        url='/register'
        data={
            "username": "wcampbell91",
            "password": "admin*8",
            "email": "billy@campbell.com",
            "first_name": "Billy",
            "last_name": "Campbell",
            "bio": "yup"
        }

        response = self.client.post(url, data, format="json")

        json_response = json.loads(response.content)

        self.token = json_response['token']

        category = Category()
        category.name="board Game"
        category.save()
        
        game = Game()
        game.categoryId = 1
        game.title = 'farts'
        game.designer = 'butts'
        game.description = 'stinky'
        game.num_players = 1
        game.year_released = 2021
        game.game_image = ''
        game.save()

        # player = Player()
        # player.user = User()
        # player.save()


    def test_create_rating(self):
        url = "/ratings"
        data = {
            'rating': 5,
            'game': 1,
            'player': 1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format="json")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json_response['game'], 1)
        self.assertEqual(json_response['player'], 1)
        self.assertEqual(json_response['rating'], 5)

    def test_change_rating(self):
        game_rating = GameRating()
        game_rating.player = Player.objects.get(pk=1)
        game_rating.game = Game.objects.get(pk=1)
        game_rating.rating = 5
        game_rating.save()

        data = {
            'player': 1,
            'game': 1,
            'rating': 9
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.put(f'/ratings/{game_rating.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(f'/ratings/{game_rating.id}')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json_response['game'], 1)
        self.assertEqual(json_response['player'], 1)
        self.assertEqual(json_response['rating'], 9)
