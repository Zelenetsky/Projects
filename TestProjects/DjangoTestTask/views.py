from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import UrlString
from .forms import UrlDataCreateForm
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    # urlobjects_number=UrlString.objects.count()
    Url_object = UrlString.objects.get(pk=1)
    
    context = {'values':[]}    
    soup=BeautifulSoup(Url_object.url_path, 'html.parser')
    html_find = soup.find_all('<html>')
    head_find = soup.find_all('<head>')
    p_find = soup.find_all('<p>')
    div_find = soup.find_all('<div>')
    context['values'] = [["<html>", len(html_find)], ["<head>", len(head_find)], ["<p>", len(p_find)], ["<div>", len(div_find)]]

    return render(request, "DjangoTestTask/home.html", context)

class UrlStringCreate(CreateView):
    model = UrlString
    template_name = 'DjangoTestTask/home.html'
    form_class = UrlDataCreateForm
