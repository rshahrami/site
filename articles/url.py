from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles_list),
    # define a variable that name is sluge
    # this variable for url articles/slug
    path('<slug>', views.articles_detail),

]