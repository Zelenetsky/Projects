from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("urldata/create", views.UrlDataCreate.as_view(), name="urldatacreate"),
]
