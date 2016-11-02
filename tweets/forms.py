from django import forms


class TweetForm(forms.Form):
    tweet_text = forms.CharField(label='Text', max_length=140)
