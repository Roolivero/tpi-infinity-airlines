from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import FlightForm

def create_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url') 
    else:
        form = FlightForm()
    return render(request, 'create_flight.html', {'form': form})