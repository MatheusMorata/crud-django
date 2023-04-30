from django.shortcuts import render
from app.models import Pessoa

def home(request):
    template = "home.html"
    pessoas = Pessoa.objects.all()
    return render(request,template,{"pessoas":pessoas})
