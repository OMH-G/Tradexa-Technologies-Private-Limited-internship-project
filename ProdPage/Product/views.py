from django.shortcuts import redirect, render,get_object_or_404
from User.models import User,Post
from .models import Product
# Create your views here.
def rawdata(usname,a=[]):
    templist=[]
    prodlist=[]
    
    for i in Post.objects.all():
        if(i.user.email==usname):
            templist.append({'pd':[i.text,1],'id':i.id})
        else:
            templist.append({'pd':[i.text,0],'id':i.id})
    for j in Product.objects.all():
        if(a==[]):
            a=[j.weight,j.price]
        if(str(j.name).endswith(usname)):
            prodlist.append({'detail':j.name.split('-')+[1]+a,'id':j.id})
        else:
            prodlist.append({'detail':j.name.split('-')+[0]+a,'id':j.id})
    return (templist,prodlist)

def index(request):
    prodlist=[]
    for i in Product.objects.all():
        posts=Post.objects.filter(text=f"Name:{i.name},Weight:{i.weight},price:{i.price}")
        user=[i.user.email for i in posts]
        print(user)
        prodlist.append([i.name,i.weight,i.price]+user)
    return render(request,'Product/front.html',{'prod':prodlist})
def ind(request):
    email=request.POST.get('email')
    password=request.POST.get('pass')
    cuser=get_object_or_404(User,email=email,password=password)
    templist,prodlist=rawdata(cuser.email)
    return render(request,'Product/postform.html',{'username':cuser.email,'allpost':templist,'prod':prodlist})
def saveproduct(request):
    productname=request.POST.get('name')
    weight=request.POST.get('weight')
    price=request.POST.get('price')
    username=request.POST.get('username')
    Product(name=f'{productname}-{username}',weight=weight,price=price).save()
    usname=get_object_or_404(User,email=username)
    templist,prodlist=rawdata(username,[weight,price])
    return render(request,'Product/postform.html',{'username':usname.email,'allpost':templist,'prod':prodlist})

def editproduct(request):
    prodid=request.POST.get('id')
    productname=request.POST.get('name')
    weight=request.POST.get('weight')
    price=request.POST.get('price')
    product=Product.objects.get(id=request.POST.get('id'))
    user=product.name.split('-')[1]
    if(productname and weight and price):
        product.name=f'{productname}-{user}'
        product.weight=weight
        product.price=price
        product.save()
        templist,prodlist=rawdata(user,[weight,price])
        return render(request,'Product/postform.html',{'username':user,'allpost':templist,'prod':prodlist})
    return render(request,'Product/prodedit.html',{'username':user,'detail':[prodid,product.name.split('-')[0],product.weight,product.price]})
def editpost(request):
    postid=request.POST.get('id')
    text=request.POST.get('text')
    user=Post.objects.get(id=postid).user.email
    print(text)
    if(text):
        get_post=Post.objects.get(id=postid)
        get_post.text=text
        get_post.save()
        templist,prodlist=rawdata(user)
        return render(request,'Product/postform.html',{'username':user,'allpost':templist,'prod':prodlist})
    return render(request,'Product/edit.html',{'username':user,'post':Post.objects.get(id=postid).text,'id':postid})

def savepost(request):
    text=request.POST.get('post')
    user=request.POST.get('username')
    Post(user=User.objects.get(email=user),text=text).save() 
    templist,prodlist=rawdata(user,[])
    return render(request,'Product/postform.html',{'username':user,'allpost':templist,'prod':prodlist})











