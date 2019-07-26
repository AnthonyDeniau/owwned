from django.db import models
from localisation.batimentmodels import Batiment

class Floor(models.Model):
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def str(self):
        return self.name
