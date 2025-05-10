from utils.serializers_base import AsyncSerializer
from .models import Category

class CategorySerializer(AsyncSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'description',
            'state',
        )

