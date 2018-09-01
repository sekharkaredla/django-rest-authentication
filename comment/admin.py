from django.contrib import admin

# Register your models here.
from comment.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','content','by_user','timestamp')
    list_editable = ('content','by_user')
