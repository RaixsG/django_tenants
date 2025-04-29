from adrf.serializers import Serializer
from rest_framework import serializers
from .models import Task

class TaskSerializer(Serializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'completed',
        )

