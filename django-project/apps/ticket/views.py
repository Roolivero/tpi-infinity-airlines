from django.shortcuts import render, get_object_or_404, redirect
from apps.flightHistory.models import FlightHistory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket
from .forms import PurchaseTicketForm
from datetime import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.


class PurchaseTicket():
    def template(request, flight_id):
        flight = get_object_or_404(FlightHistory, id=flight_id)
        
        user = request.user
        if not user.is_authenticated:
            messages.info(request, "Debe iniciar sesión para comprar un ticket.")
            request.session['flight_id'] = flight_id
            return redirect("login")
        
        flight.available_tickets = FlightHistory.objects.calculate_available_tickets(flight)

        if request.method == 'POST':
            form = PurchaseTicketForm(request.POST)
            if form.is_valid():
                quantity = form.cleaned_data['quantity']
                # Crear el ticket
                ticket = Ticket.objects.create(
                fk_date=request.fk_flight,  # Asignar la fecha actual
                ticket_class=form.ticket_class,
                purchase_date=timezone.now().date(),
                seat_location=form.seat_location,
                fk_user=request.user,
                fk_flight=flight,
                purchase_order=Ticket.get_purchase_number()  # Deberías generar un número de orden único
                )
                # Redirigir a una página de confirmación
                return redirect('purchase_confirmation', ticket_id=ticket.id)
        else:
            form = PurchaseTicketForm()
        
        return render(request, 'purchaseTicket.html', {'flight': flight, 'form' : form})
        
        
class UserTicketsView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'myTickets.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        return Ticket.objects.for_user(self.request.user)