
from django.db import models

class AirportManager(models.Manager):
    
    def by_country(self, country_name:str):
         return self.filter(fk_city__country=country_name).select_related('fk_city')
    
    

    