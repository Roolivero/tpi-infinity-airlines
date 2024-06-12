from ..models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from datetime import date
# Create your views here.


class UserTicketsView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'myTickets.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        return Ticket.objects.for_user(self.request.user).select_related('fk_flight_history', 'fk_flight__fk_route__fk_airport_departure', 'fk_flight__fk_route__fk_airport_arrival')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        return context