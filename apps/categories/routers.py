from adrf.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='category')

