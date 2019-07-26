from django.db import models


class Building(models.Model):
    name = models.DecimalField(decimal_places=2, max_digits=19)
    lat = models.DecimalField(decimal_places=2, max_digits=19)
    long = models.DecimalField(decimal_places=2, max_digits=19)

    def __str__(self):
        return self.name

