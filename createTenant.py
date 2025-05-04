import os
import django

# Configurar las variables de entorno para que Django pueda encontrar la configuración del proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.customers.models import Client, Domain

# Verifica si ya existe un tenant público
public_tenant = Client.objects.filter(schema_name='public').first()
if not public_tenant:
    # Crea el tenant público
    public_tenant = Client.objects.create(
        schema_name='public',
        name='Public Tenant',
        paid_until='2099-12-31',
    )
    
    # Asigna el dominio localhost al tenant público
    Domain.objects.create(
        tenant=public_tenant,
        domain='localhost',  # Este valor debe coincidir exactamente con la URL
        is_primary=True,
    )
    print("Tenant público creado correctamente")
else:
    # Verifica si el tenant público tiene el dominio localhost
    domain = Domain.objects.filter(tenant=public_tenant, domain='localhost').first()
    if not domain:
        Domain.objects.create(
            tenant=public_tenant,
            domain='localhost',
            is_primary=True,
        )
        print("Dominio localhost añadido al tenant público")
    else:
        print("El tenant público ya tiene el dominio localhost")

# instance = Client.objects.create(
#     schema_name="",
#     name="Main client",
#     paid_until="2099-12-31",
# )
# Domain.objects.create(
#     domain="localhost",
#     tenant=instance,
#     is_primary=True,
# )
# print("Tenant created successfully!")

# create_tenant()