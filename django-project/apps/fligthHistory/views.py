from django.shortcuts import render

class SearchFligth:
    def template(request):
        return render(request, "searchFligth.html")
    
    def templateBootstrap(request):
        return render(request, "searchFligthBts.html")
    
class FligthQuery():
    def template(request):
        return render(request, "flightQuery.html" )
