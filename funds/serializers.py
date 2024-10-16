# funds/serializers.py
from rest_framework import serializers
from .models import Fund, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class FundSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = Fund
        fields = '__all__'
