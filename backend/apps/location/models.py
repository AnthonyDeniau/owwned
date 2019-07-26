from django.db import models


class Building(models.Model):
    latitude = models.DecimalField(decimal_places=10, max_digits=15)
    longitude = models.DecimalField(decimal_places=10, max_digits=15)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
