from django.urls import path

from issue.views import GetAllIssuesAPI
urlpatterns = [
    path(r'api/issue/all',GetAllIssuesAPI.as_view(),name="get_all_issues")
]