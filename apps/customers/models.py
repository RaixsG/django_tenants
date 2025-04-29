from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


""" TENANT SCHEMA
No debe comenzar con pg_.
Debe tener entre 1 y 63 caracteres.
Puede contener letras minúsculas, números y guiones bajos (_).
No puede contener guiones (-) ni letras mayúsculas.
Por ejemplo, main, client1, tenant_abc son válidos, mientras que Main-Client, 123, pg_schema no lo son.
"""
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

