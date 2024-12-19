from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet, AddressViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('addresses', AddressViewSet)
urlpatterns = [
    path('api/v1/', include(router.urls))
]
