from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Ticket
from apps.flightHistory.models import FlightHistory
from datetime import datetime
from django.contrib import messages

class PurchaseSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'purchase_success.html'

    def post(self, request, *args, **kwargs):
        flight_id = self.kwargs.get('flight_id')
        purchase_preferences = request.session.get('purchase_preferences')
        
        if not purchase_preferences:
            messages.error(request, "No se encontraron preferencias de compra en la sesión.")
            return redirect('home')

        flight = get_object_or_404(FlightHistory, id=flight_id)
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
            purchase_order=Ticket.objects.get_new_purchase_number(),  # Generar un número de orden único
            buy_total_price=Ticket.objects.calculate_total_price(flight.fk_flight.ticket_price, quantity, ticket_class),
            quantity=quantity
        )

        FlightHistory.objects.add_sold_tickets(flight, quantity)

        extra_info = {
            'subtotal_flight_quantity': flight.fk_flight.ticket_price * float(quantity),
            'tier_class_charge': Ticket.objects.get_class_charge(ticket_class),
            'subtotal_class_quantity': Ticket.objects.get_class_charge(ticket_class) * float(quantity),
            'iva': Ticket.objects.get_iva(ticket.buy_total_price),
            'total': Ticket.objects.calculate_total_price_iva(flight.fk_flight.ticket_price, quantity, ticket_class)
        }

        extra_info['subtotal'] = extra_info['subtotal_flight_quantity'] + extra_info['subtotal_class_quantity']

        context = {
            'ticket': ticket,
            'extra_info': extra_info
        }

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return redirect('home')
