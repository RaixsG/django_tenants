import os
import django

# Configurar las variables de entorno para que Django pueda encontrar la configuración del proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.customers.models import Client, Domain

instance = Client.objects.create(
    schema_name="main_client",
    name="Main client",
    paid_until="2099-12-31",
)
Domain.objects.create(
    domain="localhost",
    tenant=instance,
    is_primary=True,
)
print("Tenant created successfully!")

# create_tenant()