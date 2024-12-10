from rest_framework import serializers
from. models import*

class CreateBookingSerializers(serializers.Serializer):
    quantity=serializers.IntegerField(default=1)
    total_price=serializers.DecimalField(max_digits=10,decimal_places=2)

class CreateUserprofileSerializers(serializers.Serializer):
    phone_number=serializers.CharField(max_length=10)

class CreatePaymentTransactionsSerializers(serializers.Serializer):
    PaymentMethod=serializers.CharField(max_length=100)
    AmountPaid=serializers.DecimalField(max_digits=5,decimal_places=2)
    TransactionID=serializers.CharField(max_length=20)
