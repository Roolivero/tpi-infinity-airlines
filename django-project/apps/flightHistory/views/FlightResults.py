from django.shortcuts import render
from apps.flightHistory.forms import QueryFlight
from apps.flight.models import Flight

class FlightResults():
    def template(request):
        if request.POST:

            flight_query = QueryFlight(request.POST)

            if flight_query.is_valid():
                
                origin = flight_query.cleaned_data['origin']
                destiny = flight_query.cleaned_data['destiny']
                date = flight_query.cleaned_data['date']
                

                result = Flight.objects.get_by_route_and_date(origin, destiny, date)
                

                return render(request, "results.html", {"result": result} )
        
        return render(request, "results.html" )
