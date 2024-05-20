from django.db import models
from apps.route.models import Route
from .manager import DepartureArrivalManager

'''
Esta tabla es la N a N para la relacion recursiva de Route
'''
class Departure_arrival(models.Model):
    fk_arrival = models.ForeignKey(Route, on_delete=models.CASCADE, null= True ,related_name='arrival_routes')
    fk_departure = models.ForeignKey(Route, on_delete=models.CASCADE, null= True, related_name='departure_routes')

    objects = DepartureArrivalManager()

    def __str__(self) -> str:
        return f"Departure  {self.fk_departure.fk_airport_departure.airport_code} - Arrival  {self.fk_arrival.fk_airport_arrival.airport_code}"