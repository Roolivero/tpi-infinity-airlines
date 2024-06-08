from django.shortcuts import render, get_object_or_404, redirect
from apps.flightHistory.models import FlightHistory
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import PurchaseTicketForm
from datetime import timezone

# Create your views here.


class PurchaseTicket():
    def template(request, flight_id):
        flight = get_object_or_404(FlightHistory, id=flight_id)
        
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
        
        
class MyTickets():
    def template(request):
        render(request='myTickets.html')
