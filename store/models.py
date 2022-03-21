import email
from email.mime import image
from enum import auto
from sre_parse import State
from django.db import models
from django.contrib.auth.models import User
from django.test import TransactionTestCase
# Create your models here.


class customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)

    def _str_(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True)
    def _str_(self):
        return self.name

    @property
    def imageURL(self):
        try:
                url = self.image.url 
        except:
                    url = ''
        return url

#image

class Order (models.Model):
    customer = models.ForeignKey(customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    def _str_(self):
        return str(self.id)
    @property
    def get_cart_total(self):
       orderitems = self.orderitem_set.all()
       total = sum([item.get_total for item in orderitems])  
       return total   

    @property
    def get_cart_total(self):
       orderitems = self.orderitem_set.all()
       total = sum([item.get_quantity for item in orderitems])  
       return total   





class orderItem(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity= models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

@property
def get_total(self):
    total = self.product.price * self.quantity
    return total


class shippingAddress(models.Model):
    customer = models.ForeignKey(customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address= models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
 

    def _str_(self):
        return self.address
