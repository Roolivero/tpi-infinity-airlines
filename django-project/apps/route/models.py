from django.db import models
from apps.airport.models import Airport
from .manager import RouteManager

class Route(models.Model):
    fk_airport_departure = models.ForeignKey(Airport, on_delete=models.CASCADE, null= False,related_name='departure_routes')
    fk_airport_arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, null= False,related_name='arrival_routes')

    objects = RouteManager()

    def __str__(self) -> str:
        return f"{self.fk_airport_departure.airport_code} - {self.fk_airport_arrival.airport_code}"
    