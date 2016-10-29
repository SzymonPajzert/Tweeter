from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    date_published = models.DateTimeField('date_published')


class Relationship(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
