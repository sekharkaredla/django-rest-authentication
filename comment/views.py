# Create your views here.

# curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:3000/data
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from comment.serializers import CommentSerializer

class commentGetAPI(APIView):
    def get(self,request,comment_id):
        comment_object = get_object_or_404(Comment,pk=comment_id)
        serialized_comment_object = CommentSerializer(comment_object)
        return Response(serialized_comment_object.data)

    def delete(self,request,comment_id):
        commentInstance = get_object_or_404(Comment,pk=comment_id)
        if commentInstance.by_user != request.user:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        commentInstance.delete()



class commentCreateAPI(APIView):
    def post(self,request):
        commentSerializer = CommentSerializer(data = request.data)
        if(commentSerializer.is_valid()):
            print(commentSerializer.validated_data)
            Comment.objects.create(**commentSerializer.validated_data)
            return HttpResponse(status=status.HTTP_202_ACCEPTED)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

class commentUpdateAPI(APIView):
    def patch(self,request,comment_id):
        commentInstance = get_object_or_404(Comment,pk=comment_id)
        if commentInstance.by_user != request.user:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        commentInstance.content = request.data.get('content')
        commentInstance.save()
        return HttpResponse(status=status.HTTP_202_ACCEPTED)



