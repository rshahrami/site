from django.shortcuts import render, HttpResponse

def about(request):
    # return HttpResponse("hello")
    return render(request=request, template_name='about.html')

def home(request):
    # return HttpResponse('home')
    return render(request=request, template_name='home.html')