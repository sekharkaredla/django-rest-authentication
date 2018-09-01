from django.conf.urls import url

from comment.views import commentGetAPI, commentCreateAPI, commentUpdateAPI

urlpatterns = [
    url(r'create', commentCreateAPI.as_view(), name="comment_create"),
    url(r'change/(?P<comment_id>\d+)', commentUpdateAPI.as_view(), name="comment_update"),
    url(r'(?P<comment_id>\d+)', commentGetAPI.as_view(), name="comment_get"),
]