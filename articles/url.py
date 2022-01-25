from django.urls import path
from . import views

# define a name for url.py
# app_name use when a url tage use in html file
app_name = "articles"

urlpatterns = [
    path('', views.articles_list, name="list"),
    # define a variable that name is slug
    # the slug variable for url articles/slug
    # define a name for path url and use in http hyperlink
    path('<slugName>', views.articles_detail, name="detail"),

]