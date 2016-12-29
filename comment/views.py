from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from comment.models import Comment

class CommentList(ListView):
    model = Comment

class CommentDetail(DetailView):
    model = Comment

class CommentCreate(CreateView):
    model = Comment
    fields = ['author', 'title', 'text']

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['author', 'title', 'text']

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment_list')