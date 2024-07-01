from django.contrib import admin
from .models import Plane

# Register your models here.

class PlaneAdmin(admin.ModelAdmin):
    list_display = ('plane_model', 'size')
    list_filter = ('plane_model',)
    search_fields = ('plane_model',)
    ordering = ('size',)

admin.site.register(Plane, PlaneAdmin)