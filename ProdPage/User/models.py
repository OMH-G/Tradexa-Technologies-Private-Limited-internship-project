from django.db import models

# Create your models here.
# User: first_name, last_name, email, password, username 
# Post: user, text, created_at, updated_at

class User(models.Model):
    first_name=models.CharField(max_length=30,null=False)
    last_name=models.CharField(max_length=30,null=False)
    username=models.CharField(max_length=30,null=False)
    email=models.EmailField(max_length=70,null=False)
    password=models.CharField(max_length=20,null=False)
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=30)
    created_at=models.DateTimeField(null=False)
    updated_at=models.DateTimeField(null=False)