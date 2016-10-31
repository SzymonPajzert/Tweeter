from django.conf.urls import url

from . import views

app_name='tweets'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^user/(?P<username>[a-zA-Z]+)/$', views.user, name='user'),
    url(r'^user/(?P<username>[a-zA-Z]+)/follow/$', views.follow, name='user_follow'),

    url(r'^tweet/(?P<tweet_id>[0-9]+)/$', views.tweet, name='tweet'),
]
