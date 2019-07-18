from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from backend.apps.team.models import Team


class Profiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
