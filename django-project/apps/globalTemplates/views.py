from django.shortcuts import render
from django.views import View

class LandingView(View):
    def template(request):
        return render(request, "landingPage.html")