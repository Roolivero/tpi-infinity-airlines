from django.contrib import admin
from .models import Flight

# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ('code', 'stopover', 'departure_time','fk_route','ticket_price')
    list_filter = ('fk_route__fk_airport_arrival__airport_code',)
    search_fields = ('code', 'departure_time')
    ordering = ('code',)

admin.site.register(Flight,FlightAdmin)