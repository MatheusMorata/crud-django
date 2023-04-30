from django.contrib import admin
from django.urls import path
from app.views import home,salvar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('salvar',salvar,name="salvar"),
]
