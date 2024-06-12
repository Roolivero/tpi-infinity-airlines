from ..forms import PurchaseTicketForm
from django.shortcuts import render, redirect
from ..models import Ticket
from apps.flightHistory.models import FlightHistory
from datetime import datetime

class PurchaseSuccess():
    '''Muestra la compra exitosa del ticket'''
    def template(request, flight_id):
        
        if request.POST:

            purchase_preferences = request.session.get('purchase_preferences')
            flight = FlightHistory.objects.get_by_id(flight_id)

            quantity = purchase_preferences['quantity']
            ticket_class = purchase_preferences['ticket_class']
            seat_location = purchase_preferences['seat_location']

            # Crear el ticket
            ticket = Ticket.objects.create(
                fk_flight_history=flight,
                ticket_class=ticket_class,
                purchase_date=datetime.now(),
                seat_location=seat_location,
                fk_user=request.user,
                fk_flight=flight.fk_flight,
                purchase_order=Ticket.objects.get_new_purchase_number(),# Deberías generar un número de orden único
                buy_total_price= (Ticket.objects.calculate_total_price(flight.fk_flight.ticket_price, quantity, ticket_class)),
                quantity=quantity
            )

            return render(request, 'purchase_success.html', {'ticket': ticket})
        else:
            return redirect('home')