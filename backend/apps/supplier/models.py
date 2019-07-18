from django.db import models


# Create your models here.
class Name(models.Model):
    name_test = models.CharField(max_length=200)
    def __str__(self):
        return self.name_test


class WebSite(models.Model):
    webSiteUrl_text = models.CharField(max_length=400)

    def __str__(self):
        return self.webSiteUrl_text

class Login(models.Model):
    login_text = models.CharField
    def __str__(self):
        return self.login_text


class Password(models.Model):
    password_text = models.CharField(max_length=20)
    def __str__(self):
        return self.password_text
