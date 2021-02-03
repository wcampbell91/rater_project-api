import json
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from raterapi.models import Category, Game, Player

class GameReviewTests(APITestCase):
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

    def test_create_review(self):
        url="/reviews"
        data = {
            'game': 1,
            'player': 1,
            'review': "this sucks"
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format="json")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json_response['game'], 1)
        self.assertEqual(json_response['player'], 1)
        self.assertEqual(json_response['review'], 'this sucks')
