from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.


class Issue(models.Model):
    topic = models.CharField(max_length=150,unique=True)
    description = models.TextField()
    likes = models.BigIntegerField(default=0)
    owner = models.ForeignKey(User,related_name="issues",on_delete=models.CASCADE,default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "issue : " + self.topic

    def __repr__(self):
        return "issue : " + self.topic+ " ,  owner : " +  str(self.owner)
