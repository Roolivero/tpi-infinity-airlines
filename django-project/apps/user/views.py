from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

class UserView:
    
    def create_user(request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User registered successfully!')
                return redirect('register')
        else:
            form = UserForm()
        return render(request, 'login.html', {'form': form})

    def login_user(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect('search_fligth')  # Redirige a la página principal o a la que desees
            else:
                messages.error(request, 'Invalid email or password')
        return render(request, 'login.html')
        
