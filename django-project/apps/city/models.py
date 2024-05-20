from django.db import models
from .manager import CityManager

class City(models.Model):
    name = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50)

    objects = CityManager()

    def __str__(self) -> str:
        return f"{self.name} - {self.country}"
    
