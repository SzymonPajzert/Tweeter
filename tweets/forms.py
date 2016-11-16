from django import forms


class TweetForm(forms.ModelForm):
    tweet_text = forms.CharField(label='Text', max_length=140)
