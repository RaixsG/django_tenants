from adrf.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from utils.serializers_base import WritableNestedModelAsyncSerializer, AsyncSerializer

from .models import Task

class TaskSerializer(WritableNestedModelAsyncSerializer):
    # category = serializers.CharField(source='category.name')
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'completed',
            'category', 
        )

class TaskListSerializer(AsyncSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'completed',
            'category', 
        )

