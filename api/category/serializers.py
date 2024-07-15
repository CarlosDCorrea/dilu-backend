from rest_framework.serializers import ModelSerializer

from .models import Category

from ..user.serializers import UserSerializer


class CategorySerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
