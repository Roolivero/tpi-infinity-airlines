from django.db import models
from .models import Fligth

class FligthManager(models.Manager):

    def without_stopover(self):
        return self.filter(stopver=False)

    def with_stopover(self):
        return self.filter(stopover=True)
    
    def by_code(self, code_input):
        return self.get(codigo=code_input)
        
    def code_exists(self, code_input) -> bool:
        return self.filter(code=code_input).exists()