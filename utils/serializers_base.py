from adrf.serializers import Serializer, ModelSerializer
from drf_writable_nested import WritableNestedModelSerializer

class AsyncSerializer(ModelSerializer):
    """
    Base serializer class that extends the Serializer class from adrf.
    This class can be used as a base for other serializers in the project.
    """
    pass

class WritableNestedModelAsyncSerializer(WritableNestedModelSerializer, ModelSerializer):
    """
    Base serializer class that extends the WritableNestedModelSerializer class from drf_writable_nested.
    This class can be used as a base for other serializers in the project.
    """
    pass