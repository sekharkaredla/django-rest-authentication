from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from issue.models import Issue
from issue.serializers import IssueSerializer


class GetAllIssuesAPI(LoginRequiredMixin,APIView):
    def get(self,request):
        all_issues = Issue.objects.all()
        serializedIssues = IssueSerializer(list(all_issues),many=True)
        return Response(data=serializedIssues.data,status=status.HTTP_200_OK)
