from ast import arg
from datetime import date
from django.shortcuts import render
from . import models
# Create your views here.


def articles_list(request):

    articles_name = models.Articles.objects.all().order_by('date')

    args = {'articles_name_arg':articles_name}
    return render(request, 'articles/articleslist.html', args)
