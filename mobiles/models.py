from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class mobiles(models.Model):
    name=models.CharField(max_length=50)
    img1=models.ImageField(upload_to='pics')
    img2=models.ImageField(upload_to='pics')
    img3=models.ImageField(upload_to='pics')
    img4=models.ImageField(upload_to='pics')
    brand=models.CharField(max_length=50)
    o_price=models.IntegerField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    ram=models.IntegerField()
    rom=models.IntegerField()
    battery=models.IntegerField()
    processor=models.CharField(max_length=50)
    os=models.CharField(max_length=50)
    f_camera=models.IntegerField()
    r_camera=models.IntegerField()

class accessories(models.Model):
    name=models.CharField(max_length=50)
    img1=models.ImageField(upload_to='pics')
    img2=models.ImageField(upload_to='pics')
    img3=models.ImageField(upload_to='pics')
    img4=models.ImageField(upload_to='pics')
    category=models.CharField(max_length=50)
    o_price=models.IntegerField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class product(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    prod_id= models.IntegerField()
    prod_type=models.CharField(max_length=11)
    quantity=models.IntegerField(default=1)
