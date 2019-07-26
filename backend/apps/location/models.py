from django.db import models


class Batiment(models.Model):
    name = models.CharField(max_length=50)
    longitude = models.DecimalField(decimal_places=3, max_digits=19)
    latitude = models.DecimalField(decimal_places=3, max_digits=19)


class Floor(models.Model):
    name = models.CharField(max_length=50)
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
