from django.urls import path
from .views.SearchFlight import SearchFlight
from .views.FlightResults import FlightResults


urlpatterns = [
    path('home/', SearchFlight.as_view(), name='search_flight'),
    path('query_flight/', FlightResults.as_view() , name='results'),
    #path('bootstrap/' , SearchFlight.templateBootstrap, name ='test_flight'),
]
    