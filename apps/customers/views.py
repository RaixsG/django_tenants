from adrf.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from .models import Client, Domain
from .serializers import ClientSerializer

@extend_schema(tags=['Client'])
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

