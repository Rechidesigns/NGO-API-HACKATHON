from rest_framework import serializers
from .models import Ngo, Blog

class NgoSerializer(serializers.ModelSerializer):
    ngo_list = serializers.ReadOnlyField()

    class Meta:
        model = Ngo
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    blog_list = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = "__all__"