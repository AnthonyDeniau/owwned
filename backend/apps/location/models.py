from django.db import models

# Create your models here.

class Batiment(models.Model):
    lat = models.DecimalField(decimal_places=2, max_digits=19)
    longBat = models.DecimalField(decimal_places=2, max_digits=19)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Floor(models.Model):
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

        
class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

