from django.shortcuts import render

# Create your views here.
def home(request):
    context={"html_tag": 5}
    return render(request, "DjangoTestTask/home.html", context)