from adrf.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()

router.register(r'tasks', TaskViewSet, basename='task')

