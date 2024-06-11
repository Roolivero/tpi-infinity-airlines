from django.urls import path
from .views.PurchaseTicket import PurchaseTicket 
from .views.UserTicketsView import UserTicketsView
from .views.PurchaseConfirmation import PurchaseConfirmation
urlpatterns = [
    path('purchase_ticket/<int:flight_id>/', PurchaseTicket.template , name='purchase'),
    path('purchase_confirmation/<int:flight_id>/', PurchaseConfirmation.template, name='purchase_confirmation'),
    path('my_tickets/', UserTicketsView.as_view(), name='user_tickets')
]