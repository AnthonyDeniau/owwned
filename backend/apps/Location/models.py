from django.db import models

# Create your models here.
class Batiment(models.Model):
    Lat = models.DecimalField
    Long = models.DecimalField
    Name = models.CharField

class Floor(models.Model):
    Batiment = models.ForeignKey('Batiment', on_delete=models.CASCADE,)
    Name = models.CharField

class Room(models.Model):
    Floor = models.ForeignKey('Floor', on_delete=models.CASCADE,)
    Name = models.CharField
