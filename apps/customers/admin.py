from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from apps.customers.models import Client

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'paid_until', 'on_trial', 'created_on')
    search_fields = ('name',)
    list_filter = ('on_trial',)
    ordering = ('-id',)

