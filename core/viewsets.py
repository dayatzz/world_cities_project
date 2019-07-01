from rest_framework import viewsets

from .models import City
from .serializers import CitySerializer, CountrySerializer


class CityViewset(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    
    def get_queryset(self):
        countries = self.request.query_params.get('countries') or ''
        if countries:
            countries = countries.split(',')
            return City.objects.filter(country__in=countries)
        return City.objects.all()


class CountryViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = CountrySerializer

    def get_queryset(self):
        return City.objects.values('country').order_by('country').distinct()