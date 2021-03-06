from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import UrlString
from .forms import UrlStringCreateForm
from bs4 import BeautifulSoup
import requests
import validators

# Create your views here.
def home(request):
     
    if UrlString.objects.exists() == True:
    # https://www.programcreek.com/python/example/68240/django.core.validators.URLValidator    
        if validators.url(UrlString.objects.last().url_path):
            Url_object = UrlString.objects.last()
        else:
            return ValueError()
    else:
        Url_object = UrlString(url_path="https://www.mysql.com/")
        Url_object.save()
        
    context = {'values':[]}
    r = requests.get(Url_object.url_path)  
    soup=BeautifulSoup(r.content, features="html.parser")

    html_find = soup.find_all('html')
    head_find = soup.find_all('head')
    p_find = soup.find_all('p')
    div_find = soup.find_all('div')
    img_find = soup.find_all('img')
    context['values'] = [["html", len(html_find)], ["head", len(head_find)], ["p", len(p_find)], ["div", len(div_find)], ["img", len(img_find)]]
    return render(request, "DjangoTestTask/home.html", context)

class UrlStringCreate(CreateView):
    model = UrlString
    template_name = 'DjangoTestTask/urldata_create_form.html'
    form_class = UrlStringCreateForm
