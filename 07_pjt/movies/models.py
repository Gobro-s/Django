from django.db import models

# Create your models here.


class Actor(models.Model):
    name = models.CharField(max_length=100)  # 배우 이름

    # movies = models.ForeignKey("Movie", on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)  # 영화 제목
    overview = models.TextField()  # 줄거리
    release_date = models.DateTimeField()  # 개봉일
    poster_path = models.TextField()  # 포스터 주소
    actors = models.ManyToManyField(Actor, symmetrical=True)


class Review(models.Model):
    title = models.CharField(max_length=100)  # 리뷰 제목
    content = models.TextField()  # 리뷰 내용
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # 외래 키 (Movie 클래스 참조)
