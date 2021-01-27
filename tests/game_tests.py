import json
from rest_framework import status
from rest_framework.test import APITestCase
from raterapi.models import Category, Game

class GameTests(APITestCase):
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
        category.name = "board Game"
        category.save()

    def test_create_game(self):
        url = "/games"
        data = {
            "title": "farts",
            "designer": "butts",
            "description": "stinky",
            "year_released": 2021,
            "num_players": 1,
            'game_image': '',
            'categoryId': 1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format="json")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json_response['title'], 'farts')
        self.assertEqual(json_response['designer'], 'butts')
        self.assertEqual(json_response['description'], 'stinky')
        self.assertEqual(json_response['year_released'], 2021)
        self.assertEqual(json_response['num_players'], 1)
        self.assertEqual(json_response['game_image'], None)

    def test_get_game(self):
        game = Game()
        game.categoryId = 1
        game.title = 'farts'
        game.designer = 'butts'
        game.description = 'stinky'
        game.num_players = 1
        game.year_released = 2021
        game.game_image = ''
        game.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        response = self.client.get(f"/games/{game.id}")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json_response['title'], 'farts')
        self.assertEqual(json_response['designer'], 'butts')
        self.assertEqual(json_response['description'], 'stinky')
        self.assertEqual(json_response['year_released'], 2021)
        self.assertEqual(json_response['num_players'], 1)
        self.assertEqual(json_response['game_image'], None)

    def test_change_game(self):
        game = Game()
        game.categoryId = 1
        game.title = 'farts'
        game.designer = 'butts'
        game.description = 'stinky'
        game.num_players = 1
        game.year_released = 2021
        game.game_image = ''
        game.save()

        data = {
            "categoryId": 1,
            "title": 'poops',
            'designer': 'butts',
            'description': 'roses',
            'num_players': 1,
            'year_released': 2021,
            'game_image': ''
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(f"/games/{game.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f'/games/{game.id}')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
