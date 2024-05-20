from django.db import models
from apps.user.models import User
from .manager import ItineraryManager

class Itinerary(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects  = ItineraryManager()

    def __str__(self) -> str:
        return f"{self.fk_user.name} - {self.fk_user.last_name}"