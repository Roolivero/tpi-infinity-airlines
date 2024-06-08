from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
'''
metodos para realizar:
-listar todos
-listar todos los vuelos que no salieron
-listar todos los vuelos que si salieron
-Realizar un queryset el cual me devuelva los vuelos dentro de un rango de fechas especifico
'''
class FlightHistoryManager(models.Manager):
    
    #join con la tabla flight para ver los detalles
    def list_all_with_flights(self):
        return self.select_related('flight_set')

    def flights_in_date_range(self, start_date, end_date):
        return self.filter(date__range=(start_date, end_date)).prefetch_related('flight_set')

    def get_by_id(self, id):
        try:
            return self.get(pk=id)
        except ObjectDoesNotExist:
            return None
    
    def update_by_id(self, id, **kwargs):
        try:
            instance = self.get(pk=id)
            for key, value in kwargs.items():
                setattr(instance, key, value)
            instance.save()
            return True
        except self.model.DoesNotExist:
            return False
    
    def delete_by_id(self, id):
        try:
            instance = self.get_by_id(id)
            instance.delete()
            return True
        except ObjectDoesNotExist:
            return False

    def list_all(self):
        return self.all()
    

    def get_by_route_and_date(self, origin, destiny, date):

        return self.select_related('fk_flight').filter(
            Q(fk_flight__fk_route__fk_airport_departure__airport_code__iexact=origin) | 
            Q(fk_flight__fk_route__fk_airport_departure__fk_city__name__iexact=origin), 
            Q(fk_flight__fk_route__fk_airport_arrival__airport_code__iexact=destiny) | 
            Q(fk_flight__fk_route__fk_airport_arrival__fk_city__name__iexact=destiny), 
            date=date
        )
    
    def calculate_available_tickets(self, flight):
         match flight.fk_plane.size:
            case 'chico':
                return 50 - flight.sold_ticket
            case 'grande':
                return 120 - flight.sold_ticket
            case _: #es mediano
                return 70 - flight.sold_ticket