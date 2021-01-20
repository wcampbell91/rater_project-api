from django.core.exceptions import ValidationError
from django.views.generic.base import View
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapi.models import Game, Category, Player, GameReview

class GamesViewSet(ViewSet):


    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            reviews = game.reviews.all()
            game.reviews.set(reviews)
            serializer = GameSerializer(game, context={"request": request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def create(self, request):
        game = Game()
        game.title = request.data["title"]
        game.designer = request.data["designer"]
        game.description = request.data["description"]
        game.year_released = request.data["year_released"]
        game.num_players = request.data["num_players"]
        game.game_image = request.data["game_image"]

        category = Category.objects.get(pk=request.data['categoryId'])
        game.category = category

        try:
            game.save()
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request):
        games = Game.objects.all()


        category = self.request.query_params.get('category', None)
        if category is not None:
            games = games.filter(category__id=category)

        serializer = GameSerializer(games, many=True, context={'request': request})
        return Response(serializer.data)
class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        url = serializers.HyperlinkedIdentityField(
            view_name='game',
            lookup_field='id'
        )
        fields = ('id', 'url', 'title', 'description', 'designer', 'year_released', 'num_players', 'game_image', 'category', 'average_rating')
        depth = 1
