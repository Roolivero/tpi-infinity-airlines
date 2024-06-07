from django.shortcuts import render

# Create your views here.

class PurchaseTicket():

    def template(request):
        render(request, 'purchaseTicket.html')
