from django.conf.urls import url

from . import views

app_name='tweets'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^user/(?P<pk>[0-9]+)/$', views.UserView.as_view(), name='user'),
    url(r'^user/(?P<pk>[0-9]+)/follow/$', views.follow, name='user_follow'),

    url(r'^tweet/(?P<pk>[0-9]+)/$', views.TweetView.as_view(), name='tweet'),

    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register')
]
