from django.db import models
import datetime
# Create your models here.
# name, weight, price, created_at, updated_at
from User.models import Post
class Product(models.Model):
    name=models.CharField(max_length=20)
    weight=models.PositiveIntegerField(null=False)
    price=models.PositiveBigIntegerField(null=False)
    created_at=models.CharField(max_length=50,default=datetime.datetime.now())
    updated_at=models.CharField(max_length=50,default=datetime.datetime.now())
    def __str__(self) -> str:
        return f'{self.name}'
