from django.db import models

# Create your models here.

class Batiment(models.Model):
   
    latitude = models.DecimalField(max_digits=25, decimal_places=25)
    longitude = models.DecimalField(max_digits=25, decimal_places=25)
    name = models.CharField(max_length = 255)

    def str(self):
        return self.name



class Floor(models.Model):
    
    batiment = models.ForeignKey(Batiment, on_delete= models.CASCADE)
    name = models.CharField(max_length = 255)

    def str(self):
        return self.name



class Room(models.Model):
    
    floor = models.ForeignKey(Floor, on_delete= models.CASCADE)
    name = models.CharField(max_length = 255)

    def str(self):
        return self.name
