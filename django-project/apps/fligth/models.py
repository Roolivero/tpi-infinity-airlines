from django.db import models
from apps.fligthHistory.models import FligthHistory
from apps.route.models import Route
from .manager import FligthManager

class Fligth(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    stopover = models.BooleanField(null=False)
    departure_time = models.TimeField()
    fk_flight_history = models.ForeignKey(FligthHistory, on_delete=models.CASCADE)
    fk_route = models.ForeignKey(Route, on_delete=models.CASCADE)

    objects = FligthManager()

