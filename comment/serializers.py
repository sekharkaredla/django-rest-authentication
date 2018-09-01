from rest_framework.serializers import ModelSerializer

from comment.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        return Comment(**validated_data)

