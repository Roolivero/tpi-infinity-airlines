from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','last_name','dni','email','password']
        
    