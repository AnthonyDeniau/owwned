from django.db import models


# Create your models here.
class Batiment(models.Model):
    lat = models.DecimalField
    long = models.DecimalField
    name = models.CharField


class Floor(models.Model):
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    name = models.CharField


class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    name = models.CharField
