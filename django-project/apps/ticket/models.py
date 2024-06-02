from django.db import models
from apps.itinerary.models import Itinerary
from apps.user.models import User
from apps.flight.models import Flight
from .manager import TicketManager
class Ticket(models.Model):
    flight_date = models.DateField()
    ticket_class = models.CharField(max_length=50) #DEFINIR CONSTRAINT
    purchase_date = models.DateField()
    seat_location = models.CharField(max_length=50) # DEFINIR BIEN 
    fk_itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    purchase_order = models.CharField(unique=True, max_length=20)

    objects = TicketManager()

    def __str__(self) -> str:
        return f"{self.flight_date} - {self.ticket_class} - {self.purchase_date} - {self.seat_location} - {self.fk_user.name} - {self.fk_user.last_name} - {self.fk_user.dni} - {self.fk_flight.code} - {self.fk_flight.departure_time} - {self.fk_flight.fk_route.fk_airport_departure.airport_code} - {self.fk_flight.fk_route.fk_airport_arrival.airport_code}"