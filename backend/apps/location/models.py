from django.db import models

class Batiment(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(decimal_places=5, max_digits=19)
    long = models.DecimalField(decimal_places=5, max_digits=19)

    def __str__(self):
        return self.name
        
class Floor(models.Model):
    name = models.CharField(max_length=200)
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name