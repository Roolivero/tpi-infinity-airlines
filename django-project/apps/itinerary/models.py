from django.db import models
from apps.user.models import User

class Itinerary(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)