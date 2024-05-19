from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import FligthForm

def create_fligth(request):
    if request.method == 'POST':
        form = FligthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url') 
    else:
        form = FligthForm()
    return render(request, 'create_fligth.html', {'form': form})