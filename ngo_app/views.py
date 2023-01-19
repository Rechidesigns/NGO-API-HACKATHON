from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog, Ngo
from .serializers import BlogSerializer
from .serializers import NgoSerializer

class NgoViewSet(viewsets.ModelViewSet):
    queryset = Ngo.objects.all()
    serializer_class = NgoSerializer
    
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()



class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
