from django.db import models
from apps.route.models import Route
from .manager import FlightManager
from .validators import validate_code
class Flight(models.Model):
    '''
    Flight sirve para realizar una plantilla de un vuelo. Su funcion es que se pueda agregar el mismo registro flight la cantidad de veces que quiera en flightHistory (siempre con fechas distintas)
    '''
    code = models.CharField(max_length=20, unique=True, validators=[validate_code])
    stopover = models.BooleanField(null=False)
    departure_time = models.TimeField()
    fk_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    ticket_price = models.FloatField(null=False, default=0)

    objects = FlightManager()

    def __str__(self) -> str:
        return f"{self.code} - {self.stopover} - {self.departure_time} - ORIGEN {self.fk_route.fk_airport_departure.airport_code} - DESTINO {self.fk_route.fk_airport_arrival.airport_code} - PRECIO {self.ticket_price}"