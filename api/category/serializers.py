from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category


class CategorySerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Category
        fields = '__all__'
