from django.urls import path
from .views import *
app_name="prod"
urlpatterns = [
    path('',newuser,name="newuser"),
    path('postform',ind,name="postform"),
    path('prodsave',saveproduct,name="prodsave"),
    path('postsave',savepost,name="postsave"),
    path('editpost',editpost,name="editpost"),
    path('editprod',editproduct,name="product"),
    path('login',index,name="login"),
]
