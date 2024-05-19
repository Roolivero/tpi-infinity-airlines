from django.db import models
'''
metodos para realizar:
-listar todos
-listar todos los vuelos que no salieron
-listar todos los vuelos que si salieron
-Realizar un queryset el cual me devuelva los vuelos dentro de un rango de fechas especifico
'''
class FligthHistoryManager(models.Manager):
    def list_all(self):
        return self.all()
    
    #join con la tabla fligth para ver los detalles
    def list_all_with_fligths(self):
        return self.select_related('fligth_set')

    def fligths_in_date_range(self, start_date, end_date):
        return self.filter(date__range=(start_date, end_date)).prefetch_related('fligth_set')
