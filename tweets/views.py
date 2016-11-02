from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Tweet, Profile


class IndexView(generic.ListView):
    template_name = 'tweets/index.html'
    context_object_name = 'tweet_list'

    def get_queryset(self):
        return Tweet.objects.filter(owner__profile__in=self.request.user.profile.followed.all())


class UserListView(generic.ListView):
    template_name = 'tweets/user_list.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.all()


class TweetView(generic.DetailView):
    model = Tweet
    template_name = 'tweets/tweet.html'


def user_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    following = user.profile in request.user.profile.followed.all()
    print("Following value is {following}".format(following=following))
    return render(request, 'tweets/user.html', {'user': user, 'following': following})


def set_follow(start_following):
    @login_required
    def follow(request, pk):
        action = "follow" if start_following else "unfollow"
        print("Trying to {action} user with id {pk} logged as {username}".
              format(pk=pk, username=request.user.username, action=action))

        followed_user = get_object_or_404(Profile, pk=pk)
        if start_following:
            request.user.profile.followed.add(followed_user)
        else:
            request.user.profile.followed.remove(followed_user)

        return HttpResponseRedirect(reverse('tweets:user_detail', args=(pk,)))

    return follow



