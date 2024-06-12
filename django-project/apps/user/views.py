from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm
from django.http import HttpResponse
from .forms import UserRegisterForm, UserLoginForm
from .models import User


class UserViews:
    def register(request):

        user = request.user
        if user.is_authenticated:
            return HttpResponse(f"{user.email} is authenticated.")
        
        context = {} #diccionario para poder enviar el error si es que existe

        if request.POST:
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email').lower()
                dni = form.cleaned_data.get('dni')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(email=email, dni=dni, password=raw_password)
                login(request, user)
                destination =  get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('search_flight')
            else:
                context['registration_form'] = form

        return render(request, 'login.html', context)

    def logout_view(request):
        logout(request)
        return redirect("home")


    def login_view(request):

        context = {}

        user = request.user

        if user.is_authenticated: 
            return redirect("search_flight")
        
        if request.POST:
            form = UserLoginForm(request.POST)
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                dni = User.objects.get_by_email(email).get_dni()

                user = authenticate(email=email, password=password, dni=dni)
                if user:
                    login(request, user)
                    destination = request.session.pop('flight_id', None)
                    if destination:
                        return redirect('purchase', flight_id=destination)
                    return redirect('search_flight')    
            else:
                context['login_form'] = form

        

        return render(request, "login.html", context)
    


def get_redirect_if_exists(request):
    redirect = None 
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect