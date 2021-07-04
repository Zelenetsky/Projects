from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path('', views.home, name="home2"),
    path('create', views.UrlStringCreate.as_view(), name="createurl"),
]
