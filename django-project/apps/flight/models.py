from django.db import models
from apps.flightHistory.models import FlightHistory
from apps.route.models import Route
from .manager import FlightManager

class Flight(models.Model):
    code = models.CharField(max_length=20, unique=True)
    stopover = models.BooleanField(null=False)
    departure_time = models.TimeField()
    fk_flight_history = models.ForeignKey(FlightHistory, on_delete=models.CASCADE)
    fk_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    ticket_price = models.FloatField(null=True)

    objects = FlightManager()

    def __str__(self) -> str:
        return f"{self.code} - {self.stopover} - {self.departure_time} - ORIGEN {self.fk_route.fk_airport_departure.airport_code} - DESTINO {self.fk_route.fk_airport_arrival.airport_code} - PRECIO {self.ticket_price}"