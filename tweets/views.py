from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from django.contrib.auth.models import User
from .models import Tweet


class IndexView(generic.ListView):
    template_name = 'tweets/index.html'

    def get_queryset(self):
        return Tweet.objects.all()


class TweetView(generic.DetailView):
    model = Tweet
    template_name = 'tweets/tweet.html'


class UserView(generic.DetailView):
    model = User
    template_name = 'tweets/user.html'


def follow(request, pk):
    if request.user.is_authenticated:
        print("Trying to follow user with id {pk} logged as {username}".format(pk=pk, username=request.user.username))
        return HttpResponseRedirect(reverse('tweets:user', args=(pk,)))
    else:
        print("Trying to follow user with id %s" % pk)
        return HttpResponseRedirect(reverse('tweets:login'))


def login(request):
    return HttpResponse("Login")


def register(request):
    return HttpResponse("Register")

