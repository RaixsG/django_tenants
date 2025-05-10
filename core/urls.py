from django.contrib import admin
from django.urls import path, include
from adrf.routers import DefaultRouter
# from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from apps.customers.routers import router as customers_router
from apps.first_data.routers import router as first_data_router
from apps.tasks.routers import router as tasks_router
from apps.categories.routers import router as categories_router

router = DefaultRouter(trailing_slash=True)

router.registry.extend(first_data_router.registry)
# router.registry.extend(customers_router.registry)
router.registry.extend(tasks_router.registry)
router.registry.extend(categories_router.registry)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)