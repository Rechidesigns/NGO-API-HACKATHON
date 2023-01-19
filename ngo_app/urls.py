from django.urls import path, include
from .views import NgoViewSet, BlogViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'ngo', NgoViewSet)
router.register(r'blog', BlogViewSet)

urlpatterns = [
    path('/', include(router.urls))
]

