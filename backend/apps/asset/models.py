from django.db import models
from backend.apps.team.models import Team
from backend.apps.supplier.models import Supplier

# Create your models here.
class Asset(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.ImageField()
    cost = models.DecimalField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

