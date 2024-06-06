from django import forms

class QueryFlight(forms.Form):
    origen = forms.CharField(
        label='Origen',
        max_length=100,
        required=True
    )
    destino = forms.CharField(
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
        origen = cleaned_data.get('origen')
        destino = cleaned_data.get('destino')

        if origen and destino and origen.lower() == destino.lower():
            raise forms.ValidationError('El origen y el destino no pueden ser el mismo.')

        return cleaned_data
