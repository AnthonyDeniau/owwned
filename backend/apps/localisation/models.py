from django.db import models


class Batiment(models.Model):
    #lat
    lat = models.DecimalField(decimal_places=4, max_digits=19)
    #long
    lng = models.DecimalField(decimal_places=4, max_digits=19)
    #name
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Floor(models.Model):
    #Batiment
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    #Name
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):
    #Batiment
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    #Name
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
