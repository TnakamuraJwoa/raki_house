from django.contrib import admin

# Register your models here.

from .models import House
from .models import Room
from .models import Reserve
from .models import Ticket
from .models import Calendar
from .models import RFourCalendar
from .models import GiveTicket



admin.site.register(House)
admin.site.register(Room)
admin.site.register(Reserve)
admin.site.register(Ticket)
admin.site.register(Calendar)
admin.site.register(RFourCalendar)
admin.site.register(GiveTicket)
