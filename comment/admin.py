from django.contrib import admin
from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)
