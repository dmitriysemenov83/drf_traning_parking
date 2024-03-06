from django.contrib import admin

from parking.models import Driver, Car, ParkingSpace


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'title', 'number')


@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = ('number', 'driver', 'car')
