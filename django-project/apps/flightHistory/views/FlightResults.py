from django.views.generic import ListView
from django.shortcuts import render
from ..forms import QueryFlightForm
from ..models import FlightHistory

class FlightResultsView(ListView):
    model = FlightHistory
    template_name = 'results.html'
    context_object_name = 'result'

    def get_queryset(self):
        origin = self.request.GET.get('origin')
        destiny = self.request.GET.get('destiny')
        date = self.request.GET.get('date')

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
            
            return result
        return FlightHistory.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QueryFlightForm(self.request.GET)
        return context
