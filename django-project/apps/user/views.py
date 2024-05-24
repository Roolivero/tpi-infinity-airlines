from django.shortcuts import render,redirect
from .forms import UserForm

class UserView:
    
    def createUser(request):
        if request.method == 'POST':
            print("post")
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('save') 
        else:
            form = UserForm()
            print("get")
            return render(request, 'login.html', {'form': form})
    
    
