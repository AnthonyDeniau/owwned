from django.db import models

# Create your models here.


class Batiment(models.Model):
    latitude = models.DecimalField(decimal_places=2, max_digits=20)
    longitude = models.DecimalField(decimal_places=2, max_digits=20)
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