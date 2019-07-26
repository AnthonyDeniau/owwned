from django.db import models
from asset.models import Asset


class Documentation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(max_length=255, blank=True, null=True)
    docfile = models.FileField(max_length=255, blank=True, null=True)

    def str(self):
        return self.name
