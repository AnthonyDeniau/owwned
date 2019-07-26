from django.contrib import admin
from .models import Batiment
from .models import Room
from .models import Floor

# Register your models here.
admin.site.register(Batiment)
admin.site.register(Floor)
admin.site.register(Room)
