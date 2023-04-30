from django.shortcuts import render
from app.models import Pessoa

def home(request):
    template = "home.html"
    pessoas = Pessoa.objects.all()
    return render(request,template,{"pessoas":pessoas})

def salvar(request):
    template = "home.html"
    nome_post = request.POST.get("nome")
    Pessoa.objects.create(nome=nome_post)
    pessoas = Pessoa.objects.all()
    return render(request,template,{"pessoas":pessoas})
