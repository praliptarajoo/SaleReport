from dataclasses import field
from rest_framework import serializers
from SaleReportApp.models import SaleData

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleData
        fields = '__all__'
