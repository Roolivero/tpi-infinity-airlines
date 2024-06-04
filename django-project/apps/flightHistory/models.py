from django.db import models
from apps.plane.models import Plane
from .manager import FlightHistoryManager

class FlightHistory(models.Model):
    date = models.DateField()
    fk_plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    sold_ticket = models.IntegerField(null=False)

    objects = FlightHistoryManager()

    def __str__(self) -> str:
        return f"{self.date} - {self.fk_plane.plane_model}"