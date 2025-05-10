from adrf.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from .models import Task
from .serializers import TaskSerializer, TaskListSerializer

@extend_schema(tags=['Task'])
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = TaskListSerializer(page, many=True)
            data = serializer.data
            return self.get_paginated_response(data)

        serializer = TaskListSerializer(queryset, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK) 

    # @transaction.atomic
    async def acreate(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            await sync_to_async(serializer.is_valid)(raise_exception=True)
            # await self.perform_acreate(serializer)
            await serializer.asave()
            data = await get_data(serializer)
            headers = self.get_success_headers(data)
            print(headers)

            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

