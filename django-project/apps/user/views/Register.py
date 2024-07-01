from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from ..forms import UserRegisterForm
from ..forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'login.html'
    success_url = reverse_lazy('search_flight')

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email').lower()
        dni = form.cleaned_data.get('dni')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(email=email, dni=dni, password=raw_password)
        if user:
            login(self.request, user)
        destination = self.get_redirect_if_exists()
        if destination:
            return redirect(destination)
        return response

    def get_redirect_if_exists(self):
        redirect = None
        if self.request.GET:
            if self.request.GET.get("next"):
                redirect = str(self.request.GET.get("next"))
        return redirect