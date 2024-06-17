from django.shortcuts import render, redirect
from django.urls import reverse

class SearchFlight():
    def template(request):
        
        errors = []

        if request.method == "POST":
            origin = request.POST.get('origin')
            destiny = request.POST.get('destiny')
            date = request.POST.get('date')

            if not origin:
                errors.append("El campo 'Origen' es obligatorio.")
            if not destiny:
                errors.append("El campo 'Destino' es obligatorio.")
            if not date:
                errors.append("El campo 'Partida' es obligatorio.")

            if errors:
                return render(request, 'searchFlight.html', {'errors': errors})

            return redirect(reverse('results') + f"?origin={origin}&destiny={destiny}&date={date}")

        return render(request, "searchFlight.html", {'errors': errors})
