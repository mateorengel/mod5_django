from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria
# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")

def categorias(request):
    items=Categoria.objects.all()
    
    return render(request, "categorias.html",{categorias:items})
