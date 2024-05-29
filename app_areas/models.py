from django.db import models

from app_products.models import Product
from app_profiles.models import Profile


class ProductionLine(models.Model):
    name = models.CharField(max_length=120)
    team_leader = models.ForeignKey(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
