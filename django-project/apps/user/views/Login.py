from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from ..forms import UserLoginForm
from ..models import User
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
    

class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('search_flight')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        dni = User.objects.get_by_email(email).get_dni()

        user = authenticate(email=email, password=password, dni=dni)
        if user:
            login(self.request, user)
            destination = self.request.session.pop('flight_id', None)
            if destination:
                return redirect('purchase', flight_id=destination)
        return super().form_valid(form)

    def get_success_url(self):
        destination = self.request.session.pop('flight_id', None)
        if destination:
            return reverse_lazy('purchase', kwargs={'flight_id': destination})
        return super().get_success_url()
