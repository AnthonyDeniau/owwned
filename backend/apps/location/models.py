from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=256)
    latitude = models.DecimalField(max_digits=25, decimal_places=5)
    longitude = models.DecimalField(max_digits=25, decimal_places=5)

    def __str__(self):
        return self.name


class Floor(models.Model):
    name = models.CharField(max_length=256)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=256)
    building = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
