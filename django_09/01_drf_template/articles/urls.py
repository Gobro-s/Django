from django.urls import path
from articles import views

urlpatterns = [
    path("articles/", views.article_list),
    path("articles/<int:article_pk>/", views.article_detail),
    # path("articles/<int:article_pk>/comments/", views.comment_create),
    path("comments/", views.comment_list),
    # 위를 특정 Article에서의 모든 댓글을 내려주는 API로 수정한다면 위 둘을 합친다.
    path("articles/<int:article_pk>/comments/", views.comment_list),
    path("comments/<int:comment_pk>/", views.comment_detail),
]
