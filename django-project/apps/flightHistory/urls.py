from django.urls import path
from .views.SearchFlight import SearchFlight
from .views.FlightQuery import FlightQuery


urlpatterns = [
    path('searchFlight/', SearchFlight.template, name='search_flight'),
    path('queryFlight/', FlightQuery.template , name='query_flight'),
    path('bootstrap/' , SearchFlight.templateBootstrap, name ='test_flight'),
]
    