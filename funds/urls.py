# funds/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FundViewSet, CompanyViewSet

router = DefaultRouter()
router.register(r'funds', FundViewSet)
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
