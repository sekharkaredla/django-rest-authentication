# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from comment.serializers import CommentSerializer

class helloApi(APIView):
    def get(self,request,comment_id):
        comment_object = Comment.objects.get(id = comment_id)
        serialized_comment_object = CommentSerializer(comment_object)
        return Response(serialized_comment_object.data)

