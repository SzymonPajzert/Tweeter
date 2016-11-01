from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from django.contrib.auth.decorators import login_required
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


@login_required
def follow(request, pk):
    print("Trying to follow user with id {pk} logged as {username}".format(pk=pk, username=request.user.username))
    return HttpResponseRedirect(reverse('tweets:user', args=(pk,)))


def login(request):
    return HttpResponse("Login")


def register(request):
    return HttpResponse("Register")

