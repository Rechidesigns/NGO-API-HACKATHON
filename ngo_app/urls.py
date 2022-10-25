

from django.urls import path
from . import views


urlpatterns = [
    path(' Ngo/', views.NgoView().as_view(), name="ngo_list"),
    path('Ngo/<int:ngo_id>/', views.NgoDetailView.as_view(), name="ngo_detail"),
    path('Blog/', views.BlogView().as_view(), name="blog_list"),
    path('Blog/<int:blog_id>/', views.BlogDetailView.as_view(), name="blog_detail"),
]