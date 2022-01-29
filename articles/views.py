from ast import arg
from datetime import date
from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.


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