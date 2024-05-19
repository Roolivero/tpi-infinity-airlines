from django.db import models

class FligthManager(models.Manager):

    def without_stopover(self):
        return self.filter(stopver=False)

    def with_stopover(self):
        return self.filter(stopover=True)
    
    def by_code(self, code_input):
        return self.get(codigo=code_input)
        
