from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

class FlightManager(models.Manager):

    def without_stopover(self):
        return self.filter(stopver=False)

    def with_stopover(self):
        return self.filter(stopover=True)
    
    def get_by_code(self, code_input):
        return self.get(codigo=code_input)
        
    def code_exists(self, code_input) -> bool:
        return self.filter(code=code_input).exists()
    
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
        
        return self.select_related(
            'fk_flight_history',
            'fk_route__fk_airport_departure',
            'fk_route__fk_airport_arrival'
            ).filter(
            # Condiciones de filtro utilizando Q
            Q(fk_route__fk_airport_departure__airport_code__iexact=origin) |  # OR
            Q(fk_route__fk_airport_departure__fk_city__name__iexact=origin),  # OR
            Q(fk_route__fk_airport_arrival__airport_code__iexact=destiny) |  # OR
            Q(fk_route__fk_airport_arrival__fk_city__name__iexact=destiny),  # OR
            fk_flight_history__date=date  # AND
    )

    def calculate_available_tickets(self, flight):
         match flight.fk_flight_history.fk_plane.size:
            case 'chico':
                return 50 - flight.fk_flight_history.sold_ticket
            case 'grande':
                return 120 - flight.fk_flight_history.sold_ticket
            case _: #es mediano
                return 70 - flight.fk_flight_history.sold_ticket