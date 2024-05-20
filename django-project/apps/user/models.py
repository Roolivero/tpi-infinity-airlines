from django.db import models
from .manager import UserManager

# Create your models here.

class User (models.Model):
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length= 100)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=False, default='')

    objects = UserManager

    def __str__(self) -> str:
        return f"{self.name} - {self.last_name} - {self.dni} - {self.email} - {self.password}"