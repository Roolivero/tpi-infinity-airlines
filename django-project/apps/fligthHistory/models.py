from django.db import models
from apps.plane.models import Plane
from .manager import FligthHistoryManager

class FligthHistory(models.Model):
    date = models.DateField()
    fk_plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

    objects = FligthHistoryManager()