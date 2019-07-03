from rest_framework import viewsets

from .models import City, Airport
from .serializers import CitySerializer, CountrySerializer, AirportSerializer


class CityViewset(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    
    def get_queryset(self):
        countries = self.request.query_params.get('countries') or ''
        if countries:
            countries = countries.split(',')
            return City.objects.filter(country__in=countries).order_by('name')
        return City.objects.all()


class CountryViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = CountrySerializer

    def get_queryset(self):
        return City.objects.values('country').order_by('country').distinct()


class AirportViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = AirportSerializer
    
    def get_queryset(self):
        countries = self.request.query_params.get('countries') or ''
        if countries:
            countries = countries.split(',')
            return Airport.objects.filter(country__in=countries).order_by('country')
        return Airport.objects.order_by('country')
