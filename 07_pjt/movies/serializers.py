from rest_framework import serializers
from .models import *


class CastingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("name",)


class ActorsmovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title",)


class ReviewmovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "title",
            "content",
        )
        read_only_fields = ("movie",)


class ActorSerializer(serializers.ModelSerializer):
    movies = ActorsmovieSerializer(read_only=True, many=True, source="movie_set")

    class Meta:
        model = Actor
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ("movie",)


class MovieSerializer(serializers.ModelSerializer):
    actors = CastingSerializer(read_only=True, many=True)
    review_set = ReviewmovieSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class MovielistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "title",
            "overview",
        )
