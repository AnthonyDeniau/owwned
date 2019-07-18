from django.db import models
from team.models import Team
from supplier.models import Supplier

# Create your models here.
class Asset(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.ImageField()
    cost = models.DecimalField(decimal_place=2, max_digits=19)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

