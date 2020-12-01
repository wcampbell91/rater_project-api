from django.core.exceptions import ValidationError
from django.views.generic.base import View
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapi.models import Game, Category, Player

class GamesViewSet(ViewSet):
    def list(self, request):
        games = Game.objects.all()

        serializer = GameSerializer(games, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        game = Game()
        game.title = request.data["title"]
        game.designer = request.data["designer"]
        game.description = request.data["description"]
        game.year_released = request.data["year_released"]
        game.num_players = request.data["num_players"]
        game.game_image = request.data["game_image"]

        try:
            game.save()
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        url = serializers.HyperlinkedIdentityField(
            view_name='game',
            lookup_field='id'
        )
        fields = ('id', 'url', 'title', 'designer', 'description', 'year_released',
        'num_players', 'game_image')
        depth = 1
