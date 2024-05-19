
from django.db import models

class AirportManager(models.Manager):
    
    def create(self, **kwargs): 
        obj = super().create(**kwargs)
        return obj
    
    def get(self, *args, **kwargs):
        obj = super().get(*args, **kwargs)
        return obj
    
    def update(self, **kwargs):
        updated_count = super().update(**kwargs)
        return updated_count
    
    def delete(self, *args, **kwargs):
        deleted_register = super().delete(*args, **kwargs)
        return deleted_register

    def getByCountry(self, country_name:str):
         return self.filter(fk_city__country=country_name).select_related('fk_city')
    
    

    