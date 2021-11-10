from django.db import models
import datetime
# Create your models here.
# User: first_name, last_name, email, password, username 
# Post: user, text, created_at, updated_at

class User(models.Model):
    first_name=models.CharField(max_length=30,null=False)
    last_name=models.CharField(max_length=30,null=False)
    username=models.CharField(max_length=30,null=False)
    email=models.EmailField(max_length=70,null=False)
    password=models.CharField(max_length=20,null=False)
    def __str__(self) -> str:
        return self.email
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=30)
    created_at=models.DateTimeField(default=datetime.datetime.now())
    updated_at=models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return self.text
