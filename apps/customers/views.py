from adrf.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from django.db import transaction

from .models import Client, Domain
from .serializers import ClientSerializer, UserSerializer

@extend_schema(tags=['Client'])
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]
    
    @transaction.atomic
    async def acreate(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            await self.sync_to_async(serializer.is_valid)(raise_exception=True)
            client = await serializer.acreate(serializer.validated_data)
            
            # Obtener serializer para la respuesta (sin incluir campos write_only)
            response_serializer = self.get_serializer(client)
            data = await self.sync_to_async(lambda: response_serializer.data)()
            
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

