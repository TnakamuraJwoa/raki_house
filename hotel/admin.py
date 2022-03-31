from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import House
from .models import Room
from .models import Reserve
from .models import Ticket
# from .models import Calendar
from .models import RFourCalendar
from .models import GiveTicket
from .models import RoomType



admin.site.register(House)
# admin.site.register(Room)
admin.site.register(Reserve)
# admin.site.register(Ticket)
# admin.site.register(Calendar)
admin.site.register(RFourCalendar)
admin.site.register(GiveTicket)
# admin.site.register(RoomType)

class TicketResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Ticket
        import_id_fields = ['Ticket_number']


@admin.register(Ticket)
class TicketAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['Ticket_number']
    # list_display = ('Ticket_number', 'issue_date', 'expiry', 'ticket_status', 'proprietary_id')

    # django-import-exportsの設定
    resource_class = TicketResource


class RoomResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Room
        import_id_fields = ['room_number']


@admin.register(Room)
class RoomAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['room_number']
    list_display = ('house_name_id', 'room_number', 'persons', 'kids', 'size', 'futon', 'Queen_bed', 'semi_Double_bed', \
                    'Double_bed', 'Single_Bed', 'smoking', 'open_bath', 'corner_room', 'ja_style', \
                    'we_style', 'dog', 'room_active', 'room_price')

    # django-import-exportsの設定
    resource_class = RoomResource



class RoomTypeResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = RoomType


@admin.register(RoomType)
class RoomTypeAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする

    # django-import-exportsの設定
    resource_class = RoomTypeResource