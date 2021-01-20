from django.core.exceptions import ValidationError
from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapi.models import GamePicture, Game
import uuid
import base64
from django.core.files.base import ContentFile



class GamePictureSerializer(serializers.ModelSerializer):
    class Meta: 
        model = GamePicture
        fields = ('id', 'game', 'action_pic')


class GamePictureViewSet(ModelViewSet):
    queryset=GamePicture.objects.all()
    serializer_class=GamePictureSerializer

    def create(self, request):
        game_picture = GamePicture()
        format, imgstr = request.data["action_pic"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["game"]}-{uuid.uuid4()}.{ext}')
        game_picture.action_pic = data
        game = Game.objects.get(pk=request.data['game'])
        game_picture.game = game

        try:
            game_picture.save()
            serializer = GamePictureSerializer(game_picture, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
