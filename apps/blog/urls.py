from __future__ import absolute_import
from django.conf.urls import url

from .views import LatestPostsView, PostsByCategoryView, PostDetailView

urlpatterns = [
    # Get Latest Blog Posts
    url(r'^$', LatestPostsView.as_view(),
        name='blog_post_latest'),

    # List News stories by a categroy
    url(r'^category/(?P<slug>[-\w]+)/$',
        PostsByCategoryView.as_view(),
        name='blog_posts_by_category'),

    # Get Post Detail
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        PostDetailView.as_view(),
        name='blog_post_detail'),

]
