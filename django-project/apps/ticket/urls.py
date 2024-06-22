from django.urls import path
from .views.PurchaseTicket import PurchaseTicketView
from .views.UserTicketsView import UserTicketsView
from .views.PurchaseConfirmation import PurchaseConfirmationView
from .views.PurchaseSuccess import PurchaseSuccessView
urlpatterns = [
    path('purchase_ticket/<int:flight_id>/', PurchaseTicketView.as_view() , name='purchase'),
    path('purchase_confirmation/<int:flight_id>/', PurchaseConfirmationView.as_view(), name='purchase_confirmation'),
    path('purchase_success/<int:flight_id>', PurchaseSuccessView.as_view(), name='purchase_success'),
    path('my_tickets/', UserTicketsView.as_view(), name='user_tickets')
]