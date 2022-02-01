from ast import arg
from re import template
import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles-url:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form_signup':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:  # the next is used in input login.html as name
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles-url:list')

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form_login':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)

        return redirect('articles-url:list')