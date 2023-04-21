from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(["GET"])
def actor_list(request):  # 전체 배우 목록 제공
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(["GET"])  # 단일 배우 정보 제공
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    movies = actor.movie_set.all()
    print(movies)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view(["GET"])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovielistSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(["GET"])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(["POST"])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)

        # return Response(status=status.HTTP_201_CREATED) 이지만,
        # 작성됐는지 페이지를 바로 확인하고 싶다.
        return Response(serializer.data)
