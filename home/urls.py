from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.signin, name="login"),
    path("logout/", views.logout_account, name="logout"),
]
