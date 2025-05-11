from asgiref.sync import sync_to_async
# from adrf.viewsets import ModelViewSet
from utils.model_viewset_customer import CustomModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from .models import Task
from .serializers import TaskSerializer, TaskListSerializer

@extend_schema(tags=['Task'])
class TaskViewSet(CustomModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    
    @sync_to_async(transaction.atomic)
    async def acreate(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            await sync_to_async(serializer.is_valid)(raise_exception=True)
            await serializer.asave()
            data = await self.get_data(serializer)
            headers = self.get_success_headers(data)
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

