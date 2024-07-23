from django.db import models
from .validators import validar_par, validation_categoria
from django.core.validators import EmailValidator
#Manejar el modelado de datos y ORM, definir tablas, objetos
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validation_categoria,])

    def __str__(self):
        return self.nombre

class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'

class Producto(models.Model):
    #nombre = models.CharField(max_length=100, unique=True, validators=[EmailValidator('No es un email valido')])
    nombre = models.CharField(max_length=100, unique=True,)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2,max_digits=10
                                 ,validators=[validar_par])
    unidades = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.UNITS
    )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.nombre