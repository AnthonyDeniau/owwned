from django.contrib import admin

from .models import Name, WebSite, Login, Password
# Register your models here.

admin.site.register(Name)
admin.site.register(WebSite)
admin.site.register(Login)
admin.site.register(Password