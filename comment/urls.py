from django.conf.urls import url
from django.urls import path

from comment.views import commentGetAPI, commentCreateAPI, getAllCommentsAPI

urlpatterns = [
    # url(r'api/comment', commentCreateAPI.as_view(), name="comment_create"),
    # url(r'api/comment/(?P<comment_id>\d+)', commentGetAPI.as_view(), name="comment_update"),
    path('api/comment/', commentCreateAPI.as_view(), name= "comment_create"),
    path('api/comment/<int:comment_id>/', commentGetAPI.as_view(), name ="comment_update_and_get"),
    path('api/comment/all/', getAllCommentsAPI.as_view(), name="get_all_comment_objects")
]