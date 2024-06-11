from django.urls import path
from .views.PurchaseTicket import PurchaseTicket 
from .views.UserTicketsView import UserTicketsView

urlpatterns = [
    path('purchase_ticket/<int:flight_id>/', PurchaseTicket.template , name='purchase'),
    path('purchase_ticket/', PurchaseTicket.template , name='purchase'),
    path('my_tickets/', UserTicketsView.as_view(), name='user_tickets')
]