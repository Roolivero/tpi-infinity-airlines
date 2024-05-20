from django.db import models
from .manager import PlaneManager
class Plane(models.Model):
    plane_model = models.CharField(max_length=50)
    SIZE = [
        ('chico', 'chico'),
        ('mediano', 'mediano'),
        ('grande', 'grande'),
    ]
    size = models.CharField(
        max_length=7,
        choices=SIZE,
        default='mediano',
    )

    objects = PlaneManager()

    def __str__(self) -> str:
        return f"{self.plane_model} - {self.size}"
