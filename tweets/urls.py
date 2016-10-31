from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user_query'),
    url(r'^user/(?P<user_id>[0-9]+)/follow/$', views.follow, name='user_follow'),

    url(r'^tweet/(?P<tweet_id>[0-9]+)/$', views.tweet, name='tweet_query'),
]
