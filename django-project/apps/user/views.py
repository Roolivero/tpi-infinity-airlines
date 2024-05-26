from django.shortcuts import render,redirect,reverse
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

class UserView:
    
    def create_user(request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User registered successfully!')
                return redirect(reverse('register'))
        else:
            form = UserForm()
        return render(request, 'login.html', {'form': form})

    def login_user(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect(reverse('search_fligth'))
            else:
                messages.error(request, 'Invalid username or password')
        return render(request, 'login.html')
        
