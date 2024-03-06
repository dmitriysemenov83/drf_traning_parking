from django.shortcuts import render
from rest_framework import viewsets

from parking.models import Driver, Car, ParkingSpace
from parking.serializers import DriverSerializer, CarSerializer, ParkingSpaceSerializer


class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class ParkingSpaceViewSet(viewsets.ModelViewSet):
    serializer_class = ParkingSpaceSerializer
    queryset = ParkingSpace.objects.all()
