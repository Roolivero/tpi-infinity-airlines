from django.shortcuts import render, get_object_or_404, redirect
from apps.flightHistory.models import FlightHistory
from django.contrib import messages
from ..models import Ticket
from ..forms import PurchaseTicketForm
from datetime import timezone
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

        form = PurchaseTicketForm()
        
        return render(request, 'purchaseTicket.html', {'flight': flight, 'form' : form})
        