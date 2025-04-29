from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField() # fecha de pago 
    on_trial = models.BooleanField(default=False) # en prueba
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True  # crea el esquema al guardar

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass
