from django.contrib.auth.models import User
from django.db import models
from issue.models import Issue

# Create your models here.



class Comment(models.Model):
    content = models.CharField(max_length=150, blank=False)
    by_user = models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.BigIntegerField(default=0)
    issue = models.ForeignKey(Issue,related_name="comments",on_delete=models.CASCADE,default=0)


    def __str__(self):
        return(self.by_user.username+" ---> "+self.content)


