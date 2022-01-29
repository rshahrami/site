from ast import arg
from re import template
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup_view(request):
    form = UserCreationForm()
    arg = {'form_signup':form}
    return render(request, 'accounts/signup.html', arg)