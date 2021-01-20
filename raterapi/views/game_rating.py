from django.http import HttpResponseServerError
from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import GameRating

class GameRatingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = GameRating
        fields = ['id', 'rating', 'game', 'player']


class GameRatingViewSet(ModelViewSet):
    queryset = GameRating.objects.all()
    serializer_class = GameRatingSerializer
