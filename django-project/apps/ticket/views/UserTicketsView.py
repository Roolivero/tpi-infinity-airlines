from ..models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.


class UserTicketsView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'myTickets.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        return Ticket.objects.for_user(self.request.user)