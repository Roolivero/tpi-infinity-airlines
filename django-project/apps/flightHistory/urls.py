from django.urls import path
from .views.SearchFlight import SearchFlight
from .views.FlightResults import FlightResults


urlpatterns = [
    path('home/', SearchFlight.template, name='search_flight'),
    path('query_flight/', FlightResults.template , name='results'),
    #path('bootstrap/' , SearchFlight.templateBootstrap, name ='test_flight'),
]
