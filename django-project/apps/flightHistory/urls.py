from django.urls import path
from .views.SearchFlight import SearchFlightView
from .views.FlightResults import FlightResultsView


urlpatterns = [
    path('', SearchFlightView.as_view(), name='search_flight'),
    path('query_flight/', FlightResultsView.as_view() , name='results'),
    #path('bootstrap/' , SearchFlight.templateBootstrap, name ='test_flight'),
]
