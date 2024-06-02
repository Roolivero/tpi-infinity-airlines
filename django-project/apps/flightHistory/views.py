from django.shortcuts import render

class SearchFlight:
    def template(request):
        return render(request, "searchFlight.html")
    
    def templateBootstrap(request):
        return render(request, "searchFlightBts.html")
    
class FlightQuery():
    def template(request):
        return render(request, "flightQuery.html" )
