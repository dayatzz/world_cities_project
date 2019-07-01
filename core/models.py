from django.db import models

class City(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    subcountry = models.CharField(max_length=50)

    def __str__(self):
        return '{} ({})'.format(self.name, self.country)
