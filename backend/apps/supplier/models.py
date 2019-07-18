from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    webStie = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

