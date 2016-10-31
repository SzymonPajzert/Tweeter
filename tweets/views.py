from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Tweet


def index(request):
    all_tweets = Tweet.objects.all()
    context = {
        'tweet_list': all_tweets,
    }
    return render(request, 'tweets/index.html', context)


def tweet(request, tweet_id):
    context = {
        'tweet': get_object_or_404(Tweet, pk=tweet_id),
    }
    return render(request, 'tweets/tweet.html', context)


def follow(request, username):
    return HttpResponse("You're trying to follow user %s" % username)


def user(request, username):
    return HttpResponse("You're looking at the details of user %s" % username)
