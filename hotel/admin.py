from django.contrib import admin

# Register your models here.

from .models import House
from .models import Room
from .models import Reserve


admin.site.register(House)
admin.site.register(Room)
admin.site.register(Reserve)