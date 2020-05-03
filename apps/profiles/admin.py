from django.contrib import admin

from .models import TrottoirUser


class TrottoirUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'last_login', 'is_superuser', 'access_user_admin')
    search_fields = ['id', 'username']
    list_display_links = ['id', 'username']
    readonly_fields = ('last_login', 'date_joined', 'last_login_ip', 'previous_login')

    fieldsets = (
        ('Personal Information', {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),
        ('Company Information', {'fields': ('company_name', 'company_address_first_line', 'company_address_second_line',
                                            'company_address_third_line', 'company_country')}),
        ('Security Options', {'fields': ('is_active', 'is_staff', 'is_superuser', 'access_user_admin')}),
        ('Account', {'fields': ('date_joined',)}),
        ('Login', {'fields': ('last_login', 'last_login_ip', 'previous_login')}),
    )


admin.site.register(TrottoirUser, TrottoirUserAdmin)
