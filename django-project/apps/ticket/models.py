from django.db import models
from apps.itinerary.models import Itinerary
from apps.user.models import User
from apps.fligth.models import Fligth

class Ticket(models.Model):
    fligth_date = models.DateField()
    ticket_class = models.CharField(max_length=50) #DEFINIR CONSTRAINT
    pourchase_date = models.DateField()
    seat_location = models.CharField(max_length=50) # DEFINIR BIEN 
    fk_itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_fligth = models.ForeignKey(Fligth, on_delete=models.CASCADE)