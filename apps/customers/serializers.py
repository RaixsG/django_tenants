from rest_framework import serializers
from utils.serializers_base import AsyncSerializer, WritableNestedModelAsyncSerializer
from django_tenants.utils import tenant_context
from asgiref.sync import sync_to_async

from .models import Client, Domain
from apps.users.models import User

class UserSerializer(AsyncSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'name',
            'last_name',
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
        )
        extra_kwargs = {
            'password': {'write_only': True}, 
        }
    
    async def acreate(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        await user.save()
        return user

class DomainSerializer(AsyncSerializer):
    class Meta:
        model = Domain
        fields = (
            'domain',
            # 'tenant',
            'is_primary',
        )

class ClientSerializer(WritableNestedModelAsyncSerializer):
    domain = DomainSerializer(source='domains', many=True)
    # user = UserSerializer(write_only=True)
    
    class Meta:
        model = Client
        fields = (
            'id',
            'name',
            'schema_name',
            'paid_until',
            'on_trial',
            'domain',
            # 'user',
        )
    
    async def acreate(self, validated_data):
        # Extraer los datos del usuario antes de crear el cliente
        domains_data = validated_data.pop('domains', [])
        
        # Crear el cliente (tenant)
        client = await Client.objects.acreate(**validated_data)
        
        # Crear dominios asociados
        for domain_data in domains_data:
            await Domain.objects.acreate(tenant=client, **domain_data)
        
        tenant_context_async = sync_to_async(tenant_context)
        
        # Preparar datos del usuario administrador
        schema_name = client.schema_name
        user_data = {
            'username': f"admin_{schema_name}",  # Username único basado en schema
            'email': f"admin@{schema_name}.com",
            'name': 'Admin',
            'last_name': schema_name.capitalize(),
            'password': 'admin123',  # Contraseña por defecto (deberías cambiarla)
            'is_superuser': True,
            'is_staff': True,
            'is_active': True
        }
        
        # Crear usuario en el contexto del tenant
        async with tenant_context_async(client):
            create_superuser = sync_to_async(User.objects.create_superuser)
            await create_superuser(
                username=user_data['username'],
                email=user_data['email'],
                name=user_data['name'],
                last_name=user_data['last_name'],
                password=user_data['password'],
                is_superuser=True,
                is_staff=True,
                is_active=user_data['is_active']
            )
        return client

