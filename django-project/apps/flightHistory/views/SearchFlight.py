from django.shortcuts import render
from django.http import HttpResponse

class SearchFlight():
    def template(request):

        if request.POST:
            return render(request, 'results.html')

        return render(request, "searchFlight.html")
    
    def templateBootstrap(request):
        return render(request, "searchFlightBts.html")

    # def templateBootstrap(request):
    #     return render(request, "searchFlightBts.html")
        