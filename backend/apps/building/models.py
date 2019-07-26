from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(decimal_places=2, max_digits=19)
    long = models.DecimalField(decimal_places=2, max_digits=19)

    def __str__(self):
        return self.name


class Floor(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)


def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
