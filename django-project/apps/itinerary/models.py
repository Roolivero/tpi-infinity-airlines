from django.db import models
from apps.user.models import User
from .manager import ItineraryManager

class Itinerary(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects  = ItineraryManager()