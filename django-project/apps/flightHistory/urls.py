from django.urls import path
from .views import SearchFlight, FlightQuery


urlpatterns = [
    path('searchFlight/', SearchFlight.template, name='search_flight'),
    path('queryFlight/', FlightQuery.template , name='query_flight'),
    path('bootstrap/' , SearchFlight.templateBootstrap, name ='test_flight'),
]
