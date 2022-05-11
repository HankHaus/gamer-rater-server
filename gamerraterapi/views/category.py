"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseServerError
from gamerraterapi.models import Category
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class CategoryView(ViewSet):

    def list(self, request):
        """Handle GET requests to get all categories

        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)



class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Category
        fields = ('id', 'label')
        depth = 1

# class CreateGameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields = ['id', 'title', 'maker', 'number_of_players', 'skill_level', 'game_type']
