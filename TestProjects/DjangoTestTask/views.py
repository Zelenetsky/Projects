from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import UrlString
from .forms import UrlStringCreateForm
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
     
    Url_object = UrlString(url_path = "https://question-it.com/questions/5825/podschet-kolichestva-tegov-html-s-pomoschju-veb-skrebkov")
    Url_object.save()
    
    context = {'values':[]}
    r = requests.get(Url_object.url_path)  
    soup=BeautifulSoup(r.content, features="html.parser")

    html_find = soup.find_all('html')
    head_find = soup.find_all('head')
    p_find = soup.find_all('p')
    div_find = soup.find_all('div')
    context['values'] = [["<html>", len(html_find)], ["<head>", len(head_find)], ["<p>", len(p_find)], ["<div>", len(div_find)]]
    return render(request, "DjangoTestTask/home.html", context)

class UrlStringCreate(CreateView):
    model = UrlString
    template_name = 'DjangoTestTask/home.html'
    form_class = UrlStringCreateForm
