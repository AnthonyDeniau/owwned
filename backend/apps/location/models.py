from django.db import models

# Create your models here.


class Batiment(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(decimal_places=3, max_digits=19)
    long = models.DecimalField(decimal_places=3, max_digits=19)

    def __str__(self):
        return self.name


class Etage(models.Model):
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Piece(models.Model):
    etage = models.ForeignKey(Etage, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


