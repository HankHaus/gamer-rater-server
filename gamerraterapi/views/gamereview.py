"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseServerError
from gamerraterapi.models import Game, Gamer, Review
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class GameReviewView(ViewSet):
    
    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized review instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.query_params.get('game', None))
        serializer = CreateReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer, game=game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        """Handle GET requests to get all reviews

        Returns:
            Response -- JSON serialized list of reviews
        """
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    
class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'review_body')




class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    """
    class Meta:
        model = Review
        fields = ('id', 'review_body', 'game')
        depth = 1



