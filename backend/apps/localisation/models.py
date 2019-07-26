from django.db import models


class Batiment(models.Model):
    lat = models.DecimalField(decimal_places=2, max_digits=19)
    long = models.DecimalField(decimal_places=2, max_digits=19)
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
