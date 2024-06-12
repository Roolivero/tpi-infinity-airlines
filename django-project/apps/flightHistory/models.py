from django.db import models
from apps.plane.models import Plane
from .manager import FlightHistoryManager
from apps.flight.models import Flight

class FlightHistory(models.Model):
    '''
    FlighHistory va a contener todos los vuelos de la aplicacion. Donde, se pueden repetir registros de la tabla Flight pero no se pueden repetir durante el mismo dia. Es importante para determinar el vuelo en especifico 
    '''
    date = models.DateField()
    fk_plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    sold_ticket = models.IntegerField(null=False)
    fk_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)

    objects = FlightHistoryManager()

    class Meta:
        unique_together = ('date', 'fk_flight')

    def __str__(self) -> str:
        return f"{self.date} - {self.fk_plane.plane_model}"