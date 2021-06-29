from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path("create", views.UrlDataCreate.as_view(), name="urldatacreate"),
]
