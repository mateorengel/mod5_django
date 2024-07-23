from django.contrib import admin
# Se manejan las configuraciones del administrador
# Register your models here.
from .models import Categoria, Producto


#""""""
#Categoria

#""""""
class CategoriaAdmin(admin.ModelAdmin):
    search_fields=('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'disponible',)
    list_filter = ('disponible', 'categoria',)
    search_fields = ('nombre',)
    ordering = ('precio',)

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)