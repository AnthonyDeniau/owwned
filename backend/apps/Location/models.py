from django.db import models

# Create your models here.


class Batiment(models.Model):
    latitude = models.DecimalField(max_digits=25, decimal_places=3)
    longitude = models.DecimalField(max_digits=25, decimal_places=3)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Floor(models.Model):

    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):

    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
