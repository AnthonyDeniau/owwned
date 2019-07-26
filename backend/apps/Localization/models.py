from django.db import models

# Create your models here.
class Building(models.Model):
    Lat = models.DecimalField(max_digits=9, decimal_places=5)
    Long = models.DecimalField(max_digits=9, decimal_places=5)
    Name = models.CharField(max_length=255)
    def __str__(self):
        return self.Name

class Floor(models.Model):
    Building = models.ForeignKey(Building, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    def __str__(self):
        return self.Name

class Room(models.Model):
    Floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    def __str__(self):
        return self.Name