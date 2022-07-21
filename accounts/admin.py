from django.contrib import admin

# Register your models here.
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "member_id",
        "gender",
        "member_type",
    )

    list_filter = (
        "member_id",
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('member_id', 'gender','member_type')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)