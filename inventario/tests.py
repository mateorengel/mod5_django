from django.test import TestCase
from django.urls.base import reverse
from .models import Categoria
from django.core.exceptions import ValidationError

# Create your tests here.

class TestCategorias(TestCase):
    
    def test_grabacion(self):
        with self.assertRaises(ValidationError) as qv: 
            q=Categoria.objects.create(nombre='No permitido')
            q.full_clean()
        mensaje_error= dict(qv.exception)
        self.assertEqual(mensaje_error["nombre"][0], "No es una opción permitida")

    #fixtures=['fixture1.json','fixture2.json', ...]
    # #configuraciones globales 
    # def setUp(self):
    #     ...
        
    # #test 1
    # def test_metodo1(self):
    #     ...
    
    
    