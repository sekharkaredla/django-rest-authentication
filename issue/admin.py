from django.contrib import admin

# Register your models here.


from issue.models import Issue

@admin.register(Issue)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','topic','description','owner')
    list_editable = ('description','owner','topic')