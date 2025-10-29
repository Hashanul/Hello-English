from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BannerViewSet, InstructionViewSet

router = DefaultRouter()
router.register('banners', BannerViewSet)
router.register('instructions', InstructionViewSet, basename='instruction')



urlpatterns = [
    path('', include(router.urls) )
]

