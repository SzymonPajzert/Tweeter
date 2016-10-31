from django.http import HttpResponse
from django.template import loader

from .models import Tweet


def index(request):
    all_tweets = Tweet.objects.all()
    template = loader.get_template('tweets/index.html')
    context = {
        'tweet_list': all_tweets,
    }
    return HttpResponse(template.render(context, request))


def tweet(request, tweet_id):
    t = Tweet.objects.get(pk=tweet_id)
    return HttpResponse("You're looking at tweet {tweet_id} with text {text}".format(tweet_id=tweet_id, text=t.text))


def follow(request, user_id):
    return HttpResponse("You're trying to follow user %s" % user_id)


def user(request, user_id):
    return HttpResponse("You're looking at the details of user %s" % user_id)
