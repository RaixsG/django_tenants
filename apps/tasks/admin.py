from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    search_fields = ('title',)

