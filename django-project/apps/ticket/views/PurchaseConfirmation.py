from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from ..forms import PurchaseTicketForm
from ..models import Ticket
from apps.flightHistory.models import FlightHistory
from datetime import datetime

class PurchaseConfirmation():
    def template(request, flight_id):
        purchase_data = PurchaseTicketForm(request.POST)
        flight = FlightHistory.objects.get_by_id(flight_id)

        if purchase_data.is_valid():

            if request.POST:
                quantity = purchase_data['quantity']
                ticket_class = purchase_data['ticket_class']
                seat_location = purchase_data['seat_location']
        
                # Crear el ticket
                ticket = Ticket.objects.create(
                fk_date=flight.date,  # Asignar la fecha actual
                ticket_class=ticket_class,
                purchase_date=datetime.now(),
                seat_location=seat_location,
                fk_user=request.user,
                fk_flight= flight,
                purchase_order=Ticket.objects.get_new_purchase_number(),# Deberías generar un número de orden único
                buy_total_price= float(Ticket.objects.calculate_total_price(flight.fk_flight.ticket_price, quantity, ticket_class)),
                quantity=quantity
                )
            else:
                render(request, 'purchase_confirmation.html', {purchase_data : 'purchase_data'})
            
        
