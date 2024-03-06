from django.urls import path, include

from parking.apps import ParkingConfig
from rest_framework.routers import DefaultRouter

from parking.views import DriverViewSet, CarViewSet, ParkingSpaceViewSet

app_name = ParkingConfig.name

dr_router = DefaultRouter()
dr_router.register(r'driver', DriverViewSet, basename='driver')

car_router = DefaultRouter()
car_router.register(r'car', CarViewSet, basename='car')

ps_router = DefaultRouter()
ps_router.register(r'parking', ParkingSpaceViewSet, basename='parking')

urlpatterns = [
    path('', include(dr_router.urls)),
    path('', include(car_router.urls)),
    path('', include(ps_router.urls)),
]
