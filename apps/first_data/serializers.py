from adrf.serializers import Serializer
from utils.serializers_base import AsyncSerializer

from apps.customers.models import Client
from apps.users.models import User

class PassSerializer(Serializer):
    pass

class SchemaClientserializer(AsyncSerializer):
    class Meta:
        model = Client
        fields = (
            'schema_name',
        )

class UserSerializer(AsyncSerializer):    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

