from django.contrib import admin

from .models import Control


class ControlAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'device', 'type', 'created_dt')
    search_fields = ('id', 'name')
    list_filter = ('device',)
    list_display_links = ('id', 'name')
    readonly_fields = ('created_dt', 'state', 'last_changed', 'user_last_changed')

    fieldsets = (
        ('Physical', {'fields': ('device', 'created_dt', 'pin_number')}),
        ('Setup', {'fields': ('name', 'type')}),
        ('Settings', {'fields': ('state', 'last_changed', 'user_last_changed')}),
    )


admin.site.register(Control, ControlAdmin)
