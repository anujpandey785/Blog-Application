from django.shortcuts import render,get_object_or_404
from main import models
from django.http import HttpResponseRedirect
from main import forms
def index(request):
    latest_articles = models.Article.objects.all().order_by('-createdAt')[:10]
    context={
        "latest_articles":latest_articles
     }
    return render(request,'main/index.html',context)


def article(request,pk):
    
    

    article=get_object_or_404(models.Article,pk=pk)

        

    context={
        "article" :article,
     }
    return render(request,'main/article.html',context)


def author(request,pk):
    author=get_object_or_404(models.Author,pk=pk)

    context ={
        "author":author
    }
    return render(request,'main/author.html',context)


def create_article(request):
    createarticle=forms.createarticleform()
    
    if request.method =="POST":
        createarticle=forms.createarticleform(request.POST)
        if createarticle.is_valid():
            createarticle.save()
            return HttpResponseRedirect("")
    context ={
        "createarticle":forms.createarticleform,
    }
    return render(request,'main/create_article.html',context)