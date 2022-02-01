from ast import arg
from datetime import date
from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms


def articles_list(request):

    # add all objects of model database to aticles_name variable
    articles_name = models.Articles.objects.all().order_by('-date')

    # define arg variable with mode database for render
    args = {'articles_name_arg':articles_name}

    # return all object of mode database with arg variable
    return render(request, 'articles/articleslist.html', args)



def articles_detail(request, slugName):
    # return HttpResponse(slugName)
    article_query = models.Articles.objects.get(slug=slugName)
    args = {'article_detail_arg':article_query}
    return render(request, 'articles/articlesdetail.html', args)



@login_required(login_url="/accounts/login")
def create_article(request):  
    if request.method=='POST':
        form=forms.CreateArticle(request.POST, request.FILES)  # the request.FILES use for get picture
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author= request.user
            instance.save()
            return redirect('articles-url:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/createarticle.html', {'form':form})