from django.apps import AppConfig
#configuracion de la applicacion 

class InventarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventario' #nombre de aplicacion. Se puede cambiar
    
    #Triggers
    #Al arrancar la app se puede verificar que ciertos aplicativos externos
