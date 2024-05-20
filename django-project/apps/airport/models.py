from django.db import models
from apps.city.models import City
from .manager import AirportManager

class Airport(models.Model):
    airport_code = models.CharField(max_length=100, unique=True, null=False)
    fk_city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)

    objects = AirportManager()

    def __str__(self) -> str:
        return f"{self.airport_code} - {self.fk_city}"