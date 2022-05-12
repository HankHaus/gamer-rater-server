"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseServerError
from gamerraterapi.models import Game
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from gamerraterapi.models import Gamer


class GameView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer)
        game = Game.objects.get(pk=serializer.data["id"])
        game.categories.add(*request.data["categories"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
        Response -- Empty body with 204 status code
        """

        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.description = request.data["description"]
        game.year_released = request.data["year_released"]
        game.number_of_players = request.data["number_of_players"]
        game.estimated_time_in_minutes = request.data["estimated_time_in_minutes"]
        game.age_recommendation = request.data["age_recommendation"]
        game.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'year_released', 'number_of_players', 'estimated_time_in_minutes', 'age_recommendation', 'gamer', 'categories')
        depth = 1

class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'year_released', 'number_of_players', 'estimated_time_in_minutes', 'age_recommendation', 'categories']
