from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'state')
    search_fields = ('name',)
    list_filter = ('state',)
    ordering = ('-id',)
    # list_per_page = 20