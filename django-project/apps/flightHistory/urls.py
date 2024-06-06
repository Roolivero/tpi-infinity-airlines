from django.urls import path
from .views.SearchFlight import SearchFlight
from .views.FlightResults import FlightResults


urlpatterns = [
    path('searchFlight/', SearchFlight.template, name='search_flight'),
    path('queryFlight/', FlightResults.template , name='results'),
    #path('bootstrap/' , SearchFlight.templateBootstrap, name ='test_flight'),
]
    