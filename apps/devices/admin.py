from django.contrib import admin

from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_dt', 'mac_address', 'added_by_user')
    search_fields = ('id', 'created_dt')
    list_filter = ('added_by_user__username',)
    list_display_links = ('id', 'name')
    readonly_fields = ('last_checkin_dt', 'created_dt')

    fieldsets = (
        ('Dates', {'fields': ('created_dt',)}),
        ('Details', {'fields': ('name', 'mac_address', 'added_by_user')}),
    )


admin.site.register(Device, DeviceAdmin)
