from django.db import models
from apps.itinerary.models import Itinerary
from apps.user.models import User
from apps.fligth.models import Fligth
from .manager import TicketManager
class Ticket(models.Model):
    fligth_date = models.DateField()
    ticket_class = models.CharField(max_length=50) #DEFINIR CONSTRAINT
    purchase_date = models.DateField()
    seat_location = models.CharField(max_length=50) # DEFINIR BIEN 
    fk_itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_fligth = models.ForeignKey(Fligth, on_delete=models.CASCADE)

    objects = TicketManager()

    def __str__(self) -> str:
        return f"{self.fligth_date} - {self.ticket_class} - {self.purchase_date} - {self.seat_location} - {self.fk_user.name} - {self.fk_user.last_name} - {self.fk_user.dni} - {self.fk_fligth.code} - {self.fk_fligth.departure_time} - {self.fk_fligth.fk_route.fk_airport_departure.airport_code} - {self.fk_fligth.fk_route.fk_airport_arrival.airport_code}"