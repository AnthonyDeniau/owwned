from django.contrib import admin

# Register your models here.
from .models import Batiment
from .models import Floor
from .models import Room

admin.site.register(Batiment)
admin.site.register(Floor)
admin.site.register(Room)
