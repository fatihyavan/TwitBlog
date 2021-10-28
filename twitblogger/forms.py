from django import forms
from tweets.models import Tweets

class twitblog(forms.ModelForm):
    class Meta:
        model=Tweets
        fields="__all__"

