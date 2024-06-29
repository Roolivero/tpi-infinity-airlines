from django.views.generic import DetailView
from apps.ticket.models import Ticket
from django.shortcuts import get_object_or_404

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'details.html'
    context_object_name = 'ticket'
    pk_url_kwarg = 'ticket_id'