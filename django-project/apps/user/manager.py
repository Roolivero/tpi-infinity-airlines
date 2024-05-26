from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class UserManager(models.Manager):

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
        
    def get_by_email(self, emial):
        try:
            return self.get(emial=emial)
        except ObjectDoesNotExist:
            return None
        
    def get_by_password(self, password):
        try:
            return self.get(password=password)
        except ObjectDoesNotExist:
            return None

    def list_all(self):
        return self.all()