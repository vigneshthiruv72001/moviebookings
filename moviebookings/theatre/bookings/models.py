from django.db import models

from movies.models import *

from django.contrib.auth.models import User

import uuid

class Booking(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    show = models.ForeignKey(Show, on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1,null = True,blank = True)
    total_price = models.DecimalField(max_digits = 10,decimal_places = 2 ,default=0.00,null = True,blank = True)
    
    def __str__(self):
        return f"{self.show} {self.id}"

class UserProfile(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey(User, on_delete = models.CASCADE,null=True,blank=True)
    phone_number = models.CharField(max_length = 10,null = True,blank = True)
    address = models.TextField(null = True,blank = True)

    def __str__(self):
        return  f"{self.user} {self.id}"

class PaymentTransactions(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    booking=models.ForeignKey(Booking, on_delete=models.CASCADE,null=True,blank=True)
    PaymentMethod=models.CharField(max_length=100,null=True,blank=True)
    AmountPaid=models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True,blank=True)
    TransactionId=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return f"{self.booking} {self.id}"