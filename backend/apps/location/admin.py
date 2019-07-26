from django.contrib import admin

from .models import Batiment, Floor, Room
# Register your models here.

admin.site.register(Batiment)
admin.site.register(Floor)
admin.site.register(Room)