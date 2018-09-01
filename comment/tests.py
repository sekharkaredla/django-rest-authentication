import django
import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'Commenter.settings'
django.setup()

from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from comment.models import Comment

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Commenter.settings")
import django
django.setup()


from django.test import TestCase

# Create your tests here.
from rest_framework import status

from rest_framework.test import APIClient

class TestComment(TestCase):
    def setUp(self):
        self.apiClient = APIClient()
        Comment.objects.create(content="test_content",by_user=User.objects.create(username = "test_use"))
    def test_getComment(self):
        url = reverse('comment_get',args = [1])
        response = self.apiClient.get(url, format = "json")
        print(response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

