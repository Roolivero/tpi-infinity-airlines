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

    