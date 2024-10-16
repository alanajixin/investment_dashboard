from django.shortcuts import render
# funds/views.py
from rest_framework import viewsets
from .models import Fund, Company
from .serializers import FundSerializer, CompanySerializer

class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


