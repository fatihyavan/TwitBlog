from django.shortcuts import render,redirect,get_object_or_404
from .models import Tweets
from twitblogger.forms import twitblog
from django.contrib import messages
from django.template import *
# noinspection PyUnusedLocal


def index(request):
    tweet=Tweets.objects.all()
    return render(request,"index.html",{"tweet":tweet})

def addTweets(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get("name")
        text = request.POST.get("text")
        newTweets =Tweets(title=title, text=text, completed=False)
        newTweets.save()
        return redirect("/")

def update(request,id):
    displayid=Tweets.objects.get(id=id)
    return render(request,"edit.html",{"displayid":displayid})

def updateMessage(request, id):
    updateMessage=Tweets.objects.get(id=id)
    form=twitblog(request.POST,instance=updateMessage)
    if form.is_valid():
        form.save()
        messages.success(request,"Update başarılı")
        return render(request, "edit.html", {"displayid": updateMessage})

def delete(request,id):
    deleteItem=Tweets.objects.get(id=id)
    deleteItem.delete()
    return redirect("/")