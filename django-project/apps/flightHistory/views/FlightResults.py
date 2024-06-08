from django.shortcuts import render
from apps.flightHistory.forms import QueryFlightForm
from ..models import FlightHistory

class FlightResults():
    def template(request):
        if request.POST:

            flight_query = QueryFlightForm(request.POST)

            if flight_query.is_valid():
                
                origin = flight_query.cleaned_data['origin']
                destiny = flight_query.cleaned_data['destiny']
                date = flight_query.cleaned_data['date']
                
                
                result = FlightHistory.objects.get_by_route_and_date(origin, destiny, date)

                for flight in result:
                    for flight in result:
                        flight.available_tickets = FlightHistory.objects.calculate_available_tickets(flight)
                
                return render(request, "results.html", {"result": result} )
        
        return render(request, "results.html" )     
