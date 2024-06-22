from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView
from django.urls import reverse_lazy
from ..models import FlightHistory, Ticket
from ..forms import PurchaseTicketForm


# class PurchaseTicket():
#     '''
#     esta vista muestra el ticket seleccionado y te permite personalizar la compra 
#     '''
#     def template(request, flight_id):
#         flight = get_object_or_404(FlightHistory, id=flight_id)
        
#         user = request.user
#         if not user.is_authenticated:
#             messages.info(request, "Debe iniciar sesión para comprar un ticket.")
#             request.session['flight_id'] = flight_id
#             return redirect("login")
        
#         flight.available_tickets = FlightHistory.objects.calculate_available_tickets(flight)

#         form = PurchaseTicketForm()
        
#         return render(request, 'purchase_ticket.html', {'flight': flight, 'form' : form})

class PurchaseTicketView(LoginRequiredMixin, DetailView, FormView):
    model = FlightHistory
    template_name = 'purchase_ticket.html'
    context_object_name = 'flight'
    form_class = PurchaseTicketForm

    def get_object(self, queryset=None):
        flight_id = self.kwargs.get('flight_id')
        flight = get_object_or_404(FlightHistory, id=flight_id)
        flight.available_tickets = FlightHistory.objects.calculate_available_tickets(flight)
        return flight

    def form_valid(self, form):
        user = self.request.user
        flight = self.get_object()
        ticket = form.save(commit=False)
        ticket.user = user
        ticket.flight = flight
        ticket.save()
        messages.success(self.request, "Ticket comprado exitosamente.")
        return redirect('ticket_detail', ticket_id=ticket.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flight'] = self.get_object()
        return context

    def handle_no_permission(self):
        messages.info(self.request, "Debe iniciar sesión para comprar un ticket.")
        self.request.session['flight_id'] = self.kwargs.get('flight_id')
        return redirect('login')
