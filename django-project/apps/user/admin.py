from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class UserAdmin(UserAdmin):
    list_display = ('email','first_name','last_name', 'dni', 'date_joined')
    list_filter = ('dni','email')
    search_fields = ('email','dni')
    readonly_fields = ('date_joined','last_login')
    ordering = ('date_joined',)
    
admin.site.register(User, UserAdmin)