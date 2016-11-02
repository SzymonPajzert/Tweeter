from django.conf.urls import url

from . import views

app_name='tweets'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^user/(?P<pk>[0-9]+)/$', views.user_view, name='user'),

    url(r'^user/(?P<pk>[0-9]+)/follow/$', views.set_follow(True), name='user_follow'),
    url(r'^user/(?P<pk>[0-9]+)/unfollow/$', views.set_follow(False), name='user_unfollow'),

    url(r'^tweet/(?P<pk>[0-9]+)/$', views.TweetView.as_view(), name='tweet'),
]
