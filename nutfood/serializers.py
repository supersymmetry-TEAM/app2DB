from rest_framework import serializers
from .models import NutData
from nutfood.models import NutData


class NutDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutData
        fields = '__all__'