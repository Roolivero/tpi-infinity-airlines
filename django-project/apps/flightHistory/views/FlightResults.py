from typing import Any
from django.shortcuts import render
from apps.flightHistory.forms import QueryFlightForm
from ..models import FlightHistory
from django.views.generic import TemplateView
class FlightResults(TemplateView):
    template_name = "results.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        modelo_vista= super().get_context_data(**kwargs)
        origin = self.request.GET.get('origin', None)
        destiny = self.request.GET.get('destiny', None)
        date = self.request.GET.get('date', None)
        # Obtener los datos de la URL

        # Crear un formulario con los datos obtenidos
        flight_query = QueryFlightForm({
            'origin': origin,
            'destiny': destiny,
            'date': date
        })

        if flight_query.is_valid():
            origin = flight_query.cleaned_data['origin']
            destiny = flight_query.cleaned_data['destiny']
            date = flight_query.cleaned_data['date']
            
            result = FlightHistory.objects.get_by_route_and_date(origin, destiny, date)

            for flight in result:
                flight.available_tickets = FlightHistory.objects.calculate_available_tickets(flight)
            
            modelo_vista["result"]=result
        return modelo_vista