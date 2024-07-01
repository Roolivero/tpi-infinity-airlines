from django.contrib import admin
from .models import Ticket

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_class','purchase_date','seat_location','fk_user','fk_flight','purchase_order','buy_total_price','quantity')
    list_filter = ('fk_user__email',)
    search_fields = ('purchase_order',)
    raw_id_fields = ('fk_user','fk_flight')

admin.site.register(Ticket,TicketAdmin)