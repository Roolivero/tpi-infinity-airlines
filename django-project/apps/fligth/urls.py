from django.urls import path
from .views import create_flight

urlpatterns = [
    path('create-flight/', create_flight, name='create_flight'),
    # Otras rutas de la aplicación
]
