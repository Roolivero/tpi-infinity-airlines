from django.db import models

class CityManager(models.Manager):

    def by_country(self, country_name:str):
        return self.filter(country=country_name)
