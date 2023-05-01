from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('',home),
    path('salvar',salvar,name="salvar"),
    path('editar/<int:id>', editar, name="editar"),
    path('atualizar/<int:id>', atualizar, name="atualizar"),
    path('deletar/<int:id>', deletar, name="deletar"),
]
