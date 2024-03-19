from django.urls import path, include
from rest_framework import routers
from api.views import ProductViewSet, PriceViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'prices', PriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
