from rest_framework.serializers import ModelSerializer

from .models import Dilu


class DiluSerializer(ModelSerializer):
    class Meta:
        model = Dilu
        fields = '__all__'
        extra_kwargs = {
            'participants': {'required': False},
            'owner': {'read_only': True}
        }
