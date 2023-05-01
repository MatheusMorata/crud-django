from django.shortcuts import render, redirect
from app.models import Pessoa

def home(request):
    template = "home.html"
    pessoa = Pessoa.objects.all()
    return render(request,template,{"pessoas":pessoa})

def salvar(request):
    template = "home.html"
    nome_post = request.POST.get("nome")
    Pessoa.objects.create(nome=nome_post)
    pessoa = Pessoa.objects.all()
    return render(request,template,{"pessoas":pessoa})

def editar(request,id):
    template = "atualizar.html"
    pessoa = Pessoa.objects.get(id=id)
    return render(request,template,{"pessoa":pessoa})

def atualizar(request,id):
    nome_post = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome_post
    pessoa.save()
    return redirect(home)

def deletar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)