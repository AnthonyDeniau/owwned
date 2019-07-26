from django.contrib import admin
from .models import Batiment
from .models import Floor
from .models import Room

# Register your models here.
admin.site.register(Batiment)
admin.site.register(Floor)
admin.site.register(Room)
