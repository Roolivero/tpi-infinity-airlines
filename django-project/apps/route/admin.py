from django.contrib import admin
from .models import Route

# Register your models here.

class RouteAdmin(admin.ModelAdmin):
    list_display = ('fk_airport_departure', 'fk_airport_arrival')
    list_filter = ('fk_airport_departure__fk_city','fk_airport_arrival__fk_city')
    raw_id_fields = ('fk_airport_departure','fk_airport_arrival')
admin.site.register(Route,RouteAdmin)
