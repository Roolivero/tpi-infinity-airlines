from django.urls import path
from .views import SearchFligth, FligthQuery


urlpatterns = [
    path('searchFligth/', SearchFligth.template, name='search_fligth'),
    path('queryFligth/', FligthQuery.template , name='search_fligth'),
]
