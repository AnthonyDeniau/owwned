from django.db import models

class Documentation(models.Model):
    # asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    url = models.URLField(max_length=255, default=None, null=True)
    docfile = models.FileField(max_length=255, default=None, null=True)
    
    def str(self):
        return self.name