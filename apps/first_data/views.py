from adrf.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from django_tenants.utils import tenant_context, schema_context, get_public_schema_name, get_tenant_domain_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from asgiref.sync import sync_to_async
from django.db import connection
from contextlib import asynccontextmanager

from apps.customers.models import Client, Domain
from apps.users.models import User
from .serializers import PassSerializer, UserSerializer

# Creamos un administrador de contexto asíncrono para el schema_context
@asynccontextmanager
async def async_schema_context(schema_name):
    """Versión asíncrona de schema_context como administrador de contexto."""
    # Obtiene el contexto de schema
    _context_manager = schema_context(schema_name)
    
    # Convierte los métodos a asíncronos
    enter_async = sync_to_async(_context_manager.__enter__)
    exit_async = sync_to_async(_context_manager.__exit__)
    
    try:
        await enter_async()
        yield
    finally:
        await exit_async(None, None, None)

@extend_schema(tags=['First Data'])
class PassViewSet(GenericViewSet):
    serializer_class = PassSerializer
    permission_classes = [AllowAny]
    
    async def create(self, request):
        """
        Crea un usuario en el tenant perteneciente al host.
        """
        try:
            # Obtener el dominio de la petición
            host = request.get_host().split(':')[0]  # Elimina el puerto si existe
            print(f"Host de la petición: {host}")
            
            # Obtener el tenant basado en el dominio
            domain_model = get_tenant_domain_model()
            domain = await sync_to_async(domain_model.objects.filter(domain=host).first)()
            
            if not domain:
                return Response({
                    "error": f"No se encontró un tenant para el dominio {host}"
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Obtener el cliente asociado al dominio
            client = await sync_to_async(lambda: domain.tenant)()
            schema_name = client.schema_name
            
            print(f"Dominio: {domain.domain}, Tenant: {client.name}, Schema: {schema_name}")
            
            # Generar datos por defecto para el usuario
            default_user_data = {
                'username': f"admin",
                'email': f"default_{schema_name}@{schema_name}.com",
                'name': f"Usuario_{schema_name}",
                'last_name': f"{schema_name}",
                'is_superuser': True,
                'is_staff': True,
                'is_active': True,
            }
            
            default_password = "admin12345"  # Contraseña predeterminada
            
            # Crear usuario dentro del contexto del tenant actual
            async with async_schema_context(schema_name):
                # Crear un nuevo usuario
                user = User(**default_user_data)
                user.set_password(default_password)
                await sync_to_async(user.save)()
                # created = True
                print("User created:", user)
            
            return Response({
                'message': 'Primera carga exitosamente',
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

