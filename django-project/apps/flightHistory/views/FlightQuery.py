from django.shortcuts import render

class FlightQuery():
    def template(request):
        return render(request, "flightQuery.html" )
