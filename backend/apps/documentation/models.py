from django.db import models

class Documentation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255)
    docfile = models.FileField(max_length=255)
    
    def str(self):
        return self.name