from django.urls import path
from . import views

# define a name for url.py
# app_name use when a url tage use in html file
app_name = "accounts-url"

urlpatterns = [
    path('signup', views.signup_view, name="signup"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),


]