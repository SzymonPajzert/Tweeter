from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Tweet


def index(request):
    context = {
        'tweet_list': Tweet.objects.all(),
    }
    return render(request, 'tweets/index.html', context)


def tweet(request, tweet_id):
    context = {
        'tweet': get_object_or_404(Tweet, pk=tweet_id),
    }
    return render(request, 'tweets/tweet.html', context)


def follow(request, username):
    print("Trying to follow %s" % username)
    return HttpResponseRedirect(reverse('tweets:user', args=(username,)))


def user(request, username):
    return render(request, 'tweets/user.html', {'user': get_object_or_404(User, username=username)})
