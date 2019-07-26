from django.db import models

class Batiment(models.Model):
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_length=255)
    long = models.DecimalField(max_length=255)
    
    def str(self):
        return self.name
