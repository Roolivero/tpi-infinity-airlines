from django.shortcuts import render

class SearchFligth:
    def template(request):
        return render(request, "searchFligth.html")
    
class FligthQuery():
    def template(request):
        return render(request, "flightQuery.html" )
