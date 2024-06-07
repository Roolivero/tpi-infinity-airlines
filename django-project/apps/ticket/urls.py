from django.urls import path
from .views import PurchaseTicket

urlpatterns = [
    path('purchase_ticket/<int:flight_id>/', PurchaseTicket.template , name='purchase'),
]