from django import forms

class QueryFlight(forms.Form):
    origin = forms.CharField(
        label='Origen',
        max_length=100,
        required=True
    )
    destiny = forms.CharField(
        label='Destino',
        max_length=100,
        required=True
    )
    date = forms.DateField(
        label='Fecha de vuelo',
        required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        origen = cleaned_data.get('origin')
        destino = cleaned_data.get('destiny')

        if origen and destino and origen.lower() == destino.lower():
            raise forms.ValidationError('El origen y el destino no pueden ser el mismo.')

        return cleaned_data
