from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",)


class ArticleListSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Nested 해서 댓글 내용 까지 출력
    comment_set = CommentSerializer(many=True, read_only=True)
    # 댓글 개수도 출력
    comment_count = serializers.IntegerField(source="comment_set.count", read_only=True)

    class Meta:
        model = Article
        # fields = ("id", "title", "content")
        fields = "__all__"

    def to_represantation(self, instance):
        rep = super().to_representation(instance)
        rep["comments"] = rep.pop("comment_set", [])
        return rep
