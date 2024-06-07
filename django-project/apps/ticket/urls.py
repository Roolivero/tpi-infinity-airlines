from django.urls import path
from .views import PurchaseTicket

urlpatterns = [
    path('purchase_ticket/', PurchaseTicket.template , name='purchase')
]