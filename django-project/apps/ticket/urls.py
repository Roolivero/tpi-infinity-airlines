from django.urls import path
from .views import PurchaseTicket, MyTickets

urlpatterns = [
    path('purchase_ticket/<int:flight_id>/', PurchaseTicket.template , name='purchase'),
    path('purchase_ticket/', PurchaseTicket.template , name='purchase'),
    path('my_tickets/', MyTickets.template, name='tickets')
]