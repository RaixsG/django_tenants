from asgiref.sync import sync_to_async
from adrf.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

class CustomModelViewSet(ModelViewSet):
    async def get_data(self, serializer):
        """Use adata if the serializer supports it, data otherwise."""
        return await serializer.adata if hasattr(serializer, "adata") else serializer.data
    
    # async def acreate(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     await sync_to_async(serializer.is_valid)(raise_exception=True)
    #     try:
    #         with transaction.atomic():
    #             # await self.perform_acreate(serializer)
    #             await serializer.asave()
    #             data = await self.get_data(serializer)
    #             headers = self.get_success_headers(data)
    #             return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    #     except Exception as e:
    #         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

