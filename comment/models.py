from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Comment(models.Model):
    content = models.CharField(max_length=150, blank=False)
    by_user = models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return(self.by_user.username+" ---> "+self.content)


