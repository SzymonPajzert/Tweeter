from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name='tweets'
urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),

    url(r'^user/$', views.UserListView.as_view(), name='user_list'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_view, name='user_detail'),

    url(r'^user/(?P<pk>[0-9]+)/follow/$', views.set_follow(True), name='user_follow'),
    url(r'^user/(?P<pk>[0-9]+)/unfollow/$', views.set_follow(False), name='user_unfollow'),

    url(r'^tweet/$', views.create_tweet, name='create_tweet'),
    url(r'^tweet/(?P<pk>[0-9]+)/$', views.TweetView.as_view(), name='tweet'),
]
