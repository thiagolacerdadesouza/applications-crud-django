from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.CommentList.as_view(),
        name='comment_list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.CommentDetail.as_view(),
        name='comment_detail'),
    url(r'^create/$',
        views.CommentCreate.as_view(),
        name='comment_create'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        views.CommentUpdate.as_view(),
        name='comment_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.CommentDelete.as_view(),
        name='comment_delete'),
]
