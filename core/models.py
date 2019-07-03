from django.db import models

class City(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    subcountry = models.CharField(max_length=50)

    def __str__(self):
        return '{} ({})'.format(self.name, self.country)


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    code = models.CharField(max_length=5)

    def __str__(self):
        return '{}: {}'.format(self.code, self.name)
