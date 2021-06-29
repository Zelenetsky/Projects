from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import UrlData
from .forms import UrlDataCreateForm

# Create your views here.
def home(request):
    context={"html_tag": 5}
    return render(request, "DjangoTestTask/home.html", context)

class UrlDataCreate(CreateView):
    model = UrlData
    template_name = 'DjangoTestTask/UrlData_create_form.html'
    form_class = UrlDataCreateForm
