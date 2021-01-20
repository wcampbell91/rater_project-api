from django.http import HttpResponseServerError
from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Player
        fields = ['id', 'user']
        depth = 1


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
