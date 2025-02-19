from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Categoria, Producto
from .form import ProductoForm
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")

def categorias(request):
    post_nombre=request.POST.get('nombre')
    
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()
        
    filtro_nombre=request.GET.get('nombre')
    if filtro_nombre:
        categorias=Categoria.objects.filter(nombre__contains=filtro_nombre)
    else:
        categorias=Categoria.objects.all()    
        
    return render(request, "form_categorias.html",{"categorias":categorias})

def productoFormView(request):
    form = ProductoForm()
    producto=None
    id_producto=request.GET.get('id')
    if id_producto:
        producto=get_object_or_404(Producto, id=id_producto)
        form=ProductoForm(instance=producto)
    
    if request.method=='POST':
        if producto:
            form=ProductoForm(request.POST, instance=producto)
        else: 
            form=ProductoForm(request.POST)
    if form.is_valid():
        form.save()
    
    return render(request, "form_productos.html",{"form":form})
