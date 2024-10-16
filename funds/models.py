from django.db import models

# Create your models here.
import uuid

class Fund(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    size_million = models.FloatField()
    total_capital_committed_billion = models.FloatField()
    global_south_deals = models.IntegerField()
    global_south_countries = models.IntegerField()

    def __str__(self):
        return self.name

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    investment_million = models.FloatField()
    country = models.CharField(max_length=255)
    country_capital_million = models.FloatField()
    theme = models.CharField(max_length=255)
    theme_capital_million = models.FloatField()
    total_emissions = models.FloatField()
    scope_1_emissions = models.FloatField()
    scope_2_emissions = models.FloatField()
    scope_3_emissions = models.FloatField()

    fund = models.ForeignKey(Fund, related_name='companies', on_delete=models.CASCADE)

    def __str__(self):
        return self.name