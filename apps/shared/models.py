from model_utils.models import TimeStampedModel
from django.db import models
from tenant_schemas.models import TenantMixin
# Create your models here.
class Tenants(TimeStampedModel, TenantMixin):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    auto_create_schema = True
    
    def __str__(self):
        return self.name

