from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.db.models import F, Sum
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
import json
from django.http import JsonResponse
# Create your views here.

@register.filter
def get_1(a):
    return 2

def home(request):

    mobs = mobiles.objects.all()
    accs = accessories.objects.all()
    count = product.objects.filter(user_id=request.user.id).count()

    return render(request, 'home.html',{'mobs':mobs,'accs':accs, 'count':count})

def mobile(request):
    
    mobs = mobiles.objects.all()
    count = product.objects.filter(user_id=request.user.id).count()
    return render(request,'mobiles.html',{'mobs':mobs,'count':count})

def accessory(request):
    
    accs = accessories.objects.all()
    count = product.objects.filter(user_id=request.user.id).count()
    return render(request,'accessories.html',{'accs':accs,'count':count})

def desc(request, value):
    count = product.objects.filter(user_id=request.user.id).count()
    if request.user.is_authenticated:
        if accessories.objects.filter(name=value).exists():
            single = accessories.objects.get(name=value)
            types='acc'
            return render(request, 'single_product.html', {'single':single, 'type':types,'count':count})
        else:
            single = mobiles.objects.get(name=value)
            types='mob'
            return render(request, 'single_product.html', {'single':single,  'type':types,'count':count})
    else:
        messages.info(request,'Login First')
        return redirect('home')


def addcart(request, pid, type):
    # if product.objects.filter(prod_id=pid, user_id=request.user.id, prod_type=type).exists():
    #     prod=product.objects.filter(prod_id=pid, user_id=request.user.id, prod_type=type).update(quantity=F('quantity')+1)
    # else:
    #     user= User.objects.get(id=request.user.id)
    #     prod=product.objects.create(prod_id=pid, user_id=user, prod_type=type)
    #     prod.save()

    if not product.objects.filter(prod_id=pid, user_id=request.user.id, prod_type=type).exists():
        user= User.objects.get(id=request.user.id)
        prod=product.objects.create(prod_id=pid, user_id=user, prod_type=type)
        prod.save()
    return redirect('cart')


def clearcart(request):
    clear=product.objects.filter(user_id=request.user.id).delete()
    return render(request,'newcart.html',{'clear':clear})

def clearProd(request, pid, type):
    product.objects.filter(prod_id=pid, user_id=request.user.id, prod_type=type).delete()
    return redirect('cart')

def cart(request):
    count = product.objects.filter(user_id=request.user.id).count()
    prod=product.objects.filter(user_id=request.user.id)
    new_prod=[]
    tot=[]
    for data in prod:
        temp={}
        temp['id']=data.id
        temp['prod_id']=data.prod_id
        temp['type']=data.prod_type
        if data.prod_type=='acc':
            acc=accessories.objects.get(pk=data.prod_id)
            temp['img1']=acc.img1
            temp['name']=acc.name
            temp['quantity']=data.quantity
            temp['price']=acc.price
            temp['total']=data.quantity*acc.price
            

        else:
            mob = mobiles.objects.get(pk=data.prod_id)
            temp['img1']=mob.img1
            temp['name']=mob.name
            temp['quantity']=data.quantity
            temp['price']=mob.price
            temp['total']=data.quantity*mob.price
        new_prod.append(temp)
        tot.append(temp['total'])
    grandTotal=sum(tot)
    return render(request,'newcart.html',{'prod':new_prod,'count':count,'grandTotal':grandTotal})

def contact(request):
    count = product.objects.filter(user_id=request.user.id).count()
    return render(request,'contactus.html',{'count':count})

def checkout(request):
    count = product.objects.filter(user_id=request.user.id).count()
    prod=product.objects.filter(user_id=request.user.id)
    new_prod=[]
    tot=[]
    for data in prod:
        temp={}

        temp['id']=data.id
        temp['prod_id']=data.prod_id
        temp['type']=data.prod_type
        if data.prod_type=='acc':
            acc=accessories.objects.get(pk=data.prod_id)
            temp['img1']=acc.img1
            temp['name']=acc.name
            temp['quantity']=data.quantity
            temp['price']=acc.price
            temp['total']=data.quantity*acc.price
            


        else:
            mob = mobiles.objects.get(pk=data.prod_id)
            temp['img1']=mob.img1
            temp['name']=mob.name
            temp['quantity']=data.quantity
            temp['price']=mob.price
            temp['total']=data.quantity*mob.price  
        new_prod.append(temp)
        tot.append(temp['total'])
    grandTotal=sum(tot)
    return render(request,'newcheckout.html',{'prod':new_prod,'count':count,'grandTotal':grandTotal})

def qtyChange(request):
    print(json.loads(request.POST['type']))
    if json.loads(request.POST['type'])=="plus":
        id = json.loads(request.POST['id'])
        product.objects.filter(id=id).update(quantity=F('quantity')+1)
        qty = product.objects.get(id=id).quantity
        price=int(json.loads(request.POST['price']))
        total=qty*price
        return JsonResponse({'qty':qty, 'total':total})
    else:
        id = json.loads(request.POST['id'])
        if product.objects.get(id=id).quantity>1:
            product.objects.filter(id=id).update(quantity=F('quantity')-1)
        qty = product.objects.get(id=id).quantity
        price=int(json.loads(request.POST['price']))
        total=qty*price
        return JsonResponse({'qty':qty, 'total':total})

def grandTotal(request):
    product.objects.aggregate(Sum('price'))


