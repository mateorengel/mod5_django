from django.contrib import admin
# Se manejan las configuraciones del administrador
# Register your models here.
from django.contrib import admin
from .models import Categoria, Producto



class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'unidades', 'disponible',)
    list_filter = ('disponible', 'categoria',)
    search_fields = ('nombre',)
    ordering = ('precio',)

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)