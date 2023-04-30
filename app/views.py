from django.shortcuts import render, redirect
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

def editar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request,"atualizar.html",{"pessoas":pessoa})

def update(request,id):
    nome_post = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome_post
    pessoa.save()
    return redirect(home)
