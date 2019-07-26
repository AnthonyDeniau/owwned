from django.db import models

# Create your models here.


class Batiment(models.Model):
    lat = models.DecimalField(decimal_places=3, max_digits=19)
    long = models.DecimalField(decimal_places=3, max_digits=19)
    name = models.CharField(max_length=255)


class Floor(models.Model):
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
