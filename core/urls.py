from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register('cities', viewsets.CityViewset, base_name='city')
router.register('countries', viewsets.CountryViewset, base_name='country')

urlpatterns = router.urls