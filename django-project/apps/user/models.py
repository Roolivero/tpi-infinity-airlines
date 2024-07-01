from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin 
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True, verbose_name=_('Email Address'))
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    dni = models.IntegerField(unique=True, verbose_name=_('Document number'))

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD="email"
    EMAIL_FIELD="email"

    REQUIRED_FIELDS= ["first_name", "last_name", "dni"]

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self) -> str:
        return f"{self.email} - {self.first_name} - {self.last_name} - {self.dni}"
    
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"
    
    def get_short_name(self):
        return self.email.split('@')[0]
    
    def get_dni(self):
        return self.dni 
    

class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField()

    def __str__(self) -> str:
        return f"{self.user.first_name}-passcode"
    
