from rest_framework import serializers
from .models import NutData
from dietrecord.models import DietRecord


class DietRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietRecord
        fields = '__all__'