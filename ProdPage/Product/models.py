from django.db import models

# Create your models here.
# name, weight, price, created_at, updated_at
class Product(models.Model):
    name=models.CharField(max_length=20)
    weight=models.PositiveIntegerField(null=False)
    price=models.PositiveBigIntegerField(null=False)
    created_at=models.DateTimeField(null=False)
    updated_at=models.DateTimeField(null=False)