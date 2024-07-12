from django.urls import path, include
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('contact/<str:name>',views.contact,name='index'),
    path('categorias/',views.categorias, name='categorias'),
    path('',views.index, name="index"),
]
