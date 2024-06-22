from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from ..forms import PurchaseTicketForm
from apps.flightHistory.models import FlightHistory
from ..models import Ticket
from django.urls import reverse_lazy


class PurchaseConfirmationView(LoginRequiredMixin, FormView):
    template_name = 'purchase_confirmation.html'
    form_class = PurchaseTicketForm

    def get_initial(self):
        initial = super().get_initial()
        flight_id = self.kwargs.get('flight_id')
        flight = get_object_or_404(FlightHistory, id=flight_id)
        initial['flight'] = flight
        return initial

    def form_valid(self, form):
        flight_id = self.kwargs.get('flight_id')
        flight = get_object_or_404(FlightHistory, id=flight_id)
        purchase_preferences = {
            'quantity': form.cleaned_data['quantity'],
            'seat_location': form.cleaned_data['seat_location'],
            'ticket_class': form.cleaned_data['ticket_class'],
            'subtotal_price_quantity': flight.fk_flight.ticket_price * float(form.cleaned_data['quantity'])
        }
        purchase_preferences['ticket_class_extra_charge'] = Ticket.objects.get_class_charge(purchase_preferences['ticket_class'])
        self.request.session['purchase_preferences'] = purchase_preferences

        total_price = Ticket.objects.calculate_total_price(
            flight.fk_flight.ticket_price,
            purchase_preferences['quantity'],
            purchase_preferences['ticket_class']
        )

        context = self.get_context_data(form=form)
        context['purchase_preferences'] = purchase_preferences
        context['flight'] = flight
        context['total_price'] = total_price
        return self.render_to_response(context)

    def form_invalid(self, form):
        return redirect('home')
