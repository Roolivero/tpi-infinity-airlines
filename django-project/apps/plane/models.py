from django.db import models
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
