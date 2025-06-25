from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet  # Добавь OrderViewSet только если он есть

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)  # Раскомментируй, если есть

urlpatterns = [
    path('', include(router.urls)),
]
