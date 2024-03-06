from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Марка')
    title = models.CharField(max_length=50, verbose_name='Название')
    number = models.IntegerField(verbose_name='Номер машины')

    def __str__(self):
        return f'{self.brand} {self.title}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class ParkingSpace(models.Model):
    number = models.IntegerField(verbose_name='Номер места')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name='Водитель')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')

    def __str__(self):
        return f'{self.number} {self.driver} {self.car}'

    class Meta:
        verbose_name = 'Парковочное место'
        verbose_name_plural = 'Парковочные места'
