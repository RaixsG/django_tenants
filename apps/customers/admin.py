from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from apps.customers.models import Client, Domain
from apps.users.models import User

class DomainInLine(admin.TabularInline):
    model = Domain
    fk_name = 'tenant'
    extra = 1
    # autocomplete_fields = ['domain',]

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    inlines = [DomainInLine,]
    list_display = ('id', 'name', 'paid_until', 'on_trial', 'created_on')
    search_fields = ('name',)
    list_filter = ('on_trial',)
    ordering = ('-id',)

@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'domain', 'tenant', 'is_primary')
    search_fields = ('domain',)
    list_filter = ('is_primary',)
    ordering = ('-id',)

