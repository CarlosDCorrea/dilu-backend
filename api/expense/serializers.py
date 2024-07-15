from rest_framework.serializers import ModelSerializer

from .models import Expense

from ..user.serializers import UserSerializer


class ExpenseSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Expense
        fields = '__all__'
