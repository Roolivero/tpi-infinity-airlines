from django.db import models
from apps.fligthHistory.models import FligthHistory
from apps.route.models import Route
from .manager import FligthManager

class Fligth(models.Model):
    code = models.CharField(max_length=20, unique=True)
    stopover = models.BooleanField(null=False)
    departure_time = models.TimeField()
    fk_fligth_history = models.ForeignKey(FligthHistory, on_delete=models.CASCADE)
    fk_route = models.ForeignKey(Route, on_delete=models.CASCADE)

    objects = FligthManager()

    def __str__(self) -> str:
        return f"{self.code} - {self.stopover} - {self.departure_time} - ORIGEN {self.fk_route.fk_airport_departure.airport_code} - DESTINO {self.fk_route.fk_airport_arrival.airport_code}"