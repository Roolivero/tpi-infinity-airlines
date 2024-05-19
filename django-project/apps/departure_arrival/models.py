from django.db import models
from apps.route.models import Route

class Departure_arrival(models.Model):
    fk_arrival = models.ForeignKey(Route, on_delete=models.CASCADE, null= True ,related_name='arrival_routes')
    fk_departure = models.ForeignKey(Route, on_delete=models.CASCADE, null= True, related_name='departure_routes')