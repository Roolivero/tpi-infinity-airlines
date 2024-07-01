from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from ..forms import QueryFlightForm

class SearchFlight(FormView):
    template_name = "searchFlight.html"
    #success_url= reverse_lazy('results')
    form_class = QueryFlightForm

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
    
        return redirect(reverse_lazy('results') + f"?origin={self.request.POST.get('origin', None)}&destiny={self.request.POST.get('destiny', None)}&date={self.request.POST.get('date', None)}")

    
    def form_invalid(self, form):
        # errors = []
        
        # origin = form.cleaned_data['origin']
        # destiny = form.cleaned_data['destiny']
        # date = form.cleaned_data['date']
        return self.render_to_response(self.get_context_data(form=form))
