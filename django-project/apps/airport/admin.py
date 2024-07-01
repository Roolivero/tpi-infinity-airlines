from django.contrib import admin

from .models import Airport
# Register your models here.
class AirportAdmin(admin.ModelAdmin):
    list_display = ('airport_code','fk_city')
    list_filter = ('fk_city',)
    search_fields = ('airport_code',)
    raw_id_fields = ('fk_city',)

admin.site.register(Airport,AirportAdmin)