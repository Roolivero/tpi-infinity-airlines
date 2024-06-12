from django.shortcuts import render, redirect
from ..forms import PurchaseTicketForm
from apps.flightHistory.models import FlightHistory
from ..models import Ticket

class PurchaseConfirmation():
    '''
    Muestra la informacion del ticket y las preferencias seleccionadas
    '''
    def template(request, flight_id):
            
        if request.POST:
            purchase_data = PurchaseTicketForm(request.POST)
            flight = FlightHistory.objects.get_by_id(flight_id)

            if purchase_data.is_valid():
                
                purchase_preferences = {
                    'quantity': purchase_data.cleaned_data['quantity'],
                    'seat_location': purchase_data.cleaned_data['seat_location'],
                    'ticket_class': purchase_data.cleaned_data['ticket_class']
                }
                request.session['purchase_preferences'] = purchase_preferences
                total_price = Ticket.objects.calculate_total_price(flight.fk_flight.ticket_price, purchase_preferences['quantity'], purchase_preferences['ticket_class'])
                
                user = request.user
                return render(request, 'purchase_confirmation.html', {'purchase_preferences' : purchase_preferences, 'flight': flight, 'user' : user, 'total_price' : total_price})
            else:
                return redirect('home')
        
        else:
            return redirect('home')
            
        
