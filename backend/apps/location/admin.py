from django.contrib import admin

# Register your models here.
from .models import Building, Floor, Room
admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Room)
