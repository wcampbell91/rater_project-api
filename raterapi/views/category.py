from django.http import HttpResponseServerError
from django.views.generic.base import View
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import Category

class CategoriesViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, context={"request": request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def list(self, request):
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True, context={"request": request})
        return Response(serializer.data)

    
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Category
        url = serializers.HyperlinkedIdentityField(
            view_name='category',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name')
