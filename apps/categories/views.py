from asgiref.sync import sync_to_async
from adrf.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from .models import Category
from .serializers import CategorySerializer

@extend_schema(tags=['Category'])
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
        
    async def adestroy(self, request, *args, **kwargs):
        instance = await self.aget_object()
        instance.state = False
        await instance.asave()
        return Response({
            "message": "ASYNC Category deleted successfully"
        }, status=status.HTTP_200_OK)

