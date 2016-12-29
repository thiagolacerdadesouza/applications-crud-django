from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse


class Comment(models.Model):
    author = models.ForeignKey(auth.models.User)
    title = models.TextField(max_length=200)
    text = models.TextField(max_length=1024)

    def get_absolute_url(self):
        return reverse('comment_detail', args=[str(self.id)])
