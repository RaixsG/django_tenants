# LEVANTAR PROYECTO
crear entorno/instalar requirements/activar entorno
- python3 manage.py makemigrations
- python3 manage.py migrate_schemas --shared
<!-- - python3 manage.py migrate_schemas -->

# Crear tenant administrador del schema public
- python3 createTenant.py

# Crear admin desde terminal
- python3 manage.py createsuperuser

# Crear admin para un tenant especifico desde terminal
- python3 manage.py tenant_command createsuperuser --schema="nombre del schema"