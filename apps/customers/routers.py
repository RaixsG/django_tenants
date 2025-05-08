from django.urls import path, include
# from rest_framework import routers
from adrf import routers

from .views import ClientViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'clients', ClientViewSet, basename='client')

