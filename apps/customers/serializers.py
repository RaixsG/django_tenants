from rest_framework import serializers
from utils.serializers_base import AsyncSerializer, WritableNestedModelAsyncSerializer

from .models import Client, Domain

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
    
    class Meta:
        model = Client
        fields = (
            'id',
            'name',
            'paid_until',
            'on_trial',
            'created_on',
            'domain',
        )

