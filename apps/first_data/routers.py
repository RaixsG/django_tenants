from django.urls import path
from adrf import routers
from .views import PassViewSet

router = routers.DefaultRouter()

router.register(r'first-data', PassViewSet, basename='first-data')

