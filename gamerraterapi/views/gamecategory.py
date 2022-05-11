"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseServerError
from gamerraterapi.models import GameCategory
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class GameCategoryView(ViewSet):

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        gamecategories = GameCategory.objects.all()
        serializer = GameCategorySerializer(gamecategories, many=True)
        return Response(serializer.data)



class GameCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = GameCategory
        fields = ('id', 'gameId', 'categoryId')
        depth = 1
