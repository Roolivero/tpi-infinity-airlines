from django import forms
from .models import Fligth
from django.core.exceptions import ValidationError
from .validators import validate_code

#Form normal de busqueda de vuelos (no visible por el usuario)
class FligthForm(forms.ModelForm):
    class Meta:
        model = Fligth
        fields = ['code', 'stopover', 'departure_time', 'fk_fligth_history', 'fk_route']

    code = forms.CharField(max_length=5, validators=[validate_code], error_messages={
        'unique' : 'A flight with this code already exists'
    })

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if Fligth.objects.code_exists():
            raise ValidationError('A flight with this code already exists.')
        return code

