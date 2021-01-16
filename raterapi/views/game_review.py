from django.http import HttpResponseServerError
from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import GameReview

class GameReviewSerializer(serializers.ModelSerializer):
    class Meta: 
        model = GameReview
        fields = ['id', 'review', 'game', 'player']


class GameReviewViewSet(ModelViewSet):
    queryset = GameReview.objects.all()
    serializer_class = GameReviewSerializer
