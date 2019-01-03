# Create your views here.

# curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:3000/data
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from comment.serializers import CommentSerializer


class commentGetAPI(LoginRequiredMixin,APIView):
    def get(self,request,comment_id):
        comment_object = get_object_or_404(Comment,pk=comment_id)
        serialized_comment_object = CommentSerializer(comment_object)
        return Response(serialized_comment_object.data)

    def delete(self,request,comment_id):
        commentInstance = get_object_or_404(Comment,pk=comment_id)
        if commentInstance.by_user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        commentInstance.delete()

    def patch(self, request, comment_id):
        commentInstance = get_object_or_404(Comment, pk=comment_id)
        if commentInstance.by_user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        commentInstance.content = request.data.get('content')
        commentInstance.save()
        return Response(status=status.HTTP_202_ACCEPTED)



class commentCreateAPI(LoginRequiredMixin,APIView):
    def post(self,request):
        commentSerializer = CommentSerializer(data = request.data)
        if(commentSerializer.is_valid()):
            print(commentSerializer.validated_data)
            # Comment.objects.create(**commentSerializer.validated_data)
            CommentSerializer.create(**commentSerializer.validated_data)
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class getAllCommentsAPI(LoginRequiredMixin,APIView):
    def get(self,request):
        comment_objects = Comment.objects.all()
        print(list(comment_objects)) # to convert queryset to list of objects, queryset is lazy, it has to be iterred thorugh so as to get the objects which can serialized
        serialized_comment_objects = CommentSerializer(comment_objects, many=True)
        return Response(serialized_comment_objects.data)


class likeCommentAPI(LoginRequiredMixin,APIView):
    def get(self,request,comment_id):
        try:
            comment_object = get_object_or_404(Comment,pk=comment_id)
        except Http404 as err:
            return Response(status=status.HTTP_404_NOT_FOUND)
        comment_object.likes += 1
        comment_object.save()
        return Response(status=status.HTTP_202_ACCEPTED)






