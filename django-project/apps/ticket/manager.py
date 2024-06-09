from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

class TicketManager(models.Manager):

    purchase_number = 0

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
    
    def get_purchase_number():
        TicketManager.purchase_number = TicketManager.purchase_number + 1
        return  TicketManager.purchase_number
    
    def for_user(self, user):
        return self.filter(fk_user=user)
