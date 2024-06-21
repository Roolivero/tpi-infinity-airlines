from django.contrib import admin
from .models import City

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('name','country')
    list_filter = ('name','country')
    search_fields = ('name','country')
    ordering = ('name',)

admin.site.register(City,CityAdmin)
