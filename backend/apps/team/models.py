from django.contrib.auth.models import User
from django.db import models
from organization.models import Organization


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name