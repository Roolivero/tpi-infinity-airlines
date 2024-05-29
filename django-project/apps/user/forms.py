from django import forms
from django.db import models

class UserForm(forms.Form):
    email= models.EmailField(max_length=50, unique=True)
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    password= models.CharField(max_length=60)
    dni = models.IntegerField(unique=True)
