from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Expense

from ..user.serializers import UserSerializer


class ExpenseSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Expense
        fields = '__all__'

    def validate(self, attr):
        extra_fields = set(self.initial_data) - set(self.fields)

        if extra_fields:
            raise serializers.ValidationError(
                f'wrong fields provided {extra_fields}')

        return attr


class ExpenseGraphSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = ['value', 'created']
