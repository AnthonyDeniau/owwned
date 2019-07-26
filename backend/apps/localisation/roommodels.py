from django.db import models
from localisation.floormodels import Floor

class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def str(self):
        return self.name
