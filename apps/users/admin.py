from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import User

@admin.register(User)
class UserAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'is_active', 'is_staff')
    search_fields = ('username',)
    list_filter = ('is_active', 'is_staff')
    ordering = ('-id',)
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'name', 'last_name', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )

