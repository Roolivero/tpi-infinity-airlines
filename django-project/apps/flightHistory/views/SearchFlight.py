from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from ..forms import QueryFlightForm

class SearchFlightView(FormView):
    template_name = 'searchFlight.html'
    form_class = QueryFlightForm

    def form_valid(self, form):
        origin = form.cleaned_data['origin']
        destiny = form.cleaned_data['destiny']
        date = form.cleaned_data['date']

        # Construir la query string para redirigir con los parámetros
        query_string = f"?origin={origin}&destiny={destiny}&date={date}"
        return redirect(reverse('results') + query_string)
