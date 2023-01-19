from django.urls import path, include
from .views import LogoutView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView




urlpatterns = [
    path('admin/login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('refresh', TokenRefreshView().as_view(), name="refresh_token"),
    path('auth/', include('djoser.urls')),
]