from django.db import models
from team.models import Team

from supplier.models import Supplier
from location.models import Room


# Create your models here.
class Asset(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.ImageField()
    cost = models.DecimalField(decimal_places=2, max_digits=19)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name