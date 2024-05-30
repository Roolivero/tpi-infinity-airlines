from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django import forms
from .models import User


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(max_length=255, required=False, help_text="Requiered. Add a valid email address.")
    class Meta:

        model = User
        fields = ['email', 'first_name', 'last_name', 'dni', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use")
    
    def clean_dni(self):
        dni = self.cleaned_data['dni']
        try:
            user = User.objects.get(dni=dni)
        except Exception as e:
            return dni
        raise forms.ValidationError(f"Dni {dni} is already in use")

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ("email", "password")


    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
