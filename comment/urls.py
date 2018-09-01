from django.conf.urls import url

from comment.views import helloApi

urlpatterns = [
    url(r'(?P<comment_id>\d+)', helloApi.as_view(), name="comment_get")
]