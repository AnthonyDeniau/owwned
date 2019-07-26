from django.db import models
from django.contrib.auth.models import User
from asset.models import Asset

class HistoryEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    CHOICES = [
        ('Lend', 'Lend'),
        ('Maintenance', 'Maintenance'),
        ('Other', 'Other'),
    ]
    typeEvent = models.CharField(
        max_length=30,
        choices=CHOICES,
        default='Other',
    )
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return "History asset:" + " user: " + self.user.username

