from django.contrib import admin
from .models import FlightHistory

# Register your models here.

class FlightHistoryAdmin(admin.ModelAdmin):
    list_display = ('date', 'fk_plane', 'sold_ticket','fk_flight')
    list_filter = ('fk_plane','fk_flight')
    search_fields = ('date',)
    ordering = ('date',)

admin.site.register(FlightHistory,FlightHistoryAdmin)