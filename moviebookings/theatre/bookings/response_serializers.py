from rest_framework import serializers
from.models import*
from django.contrib.auth.models import User

class BookingSerializers(serializers.ModelSerializer):

    show = serializers.SerializerMethodField()
    user=serializers.SerializerMethodField()

    class Meta:
        model=Booking
        fields=["show","user","quantity","total_price"]

    def get_show(self,obj):
        return {"title":obj.show.movie.title}
    def get_user(self,obj):
        return {"username":obj.user.username}
    
   
         
class UserprofileSerializers(serializers.ModelSerializer):
 
    user=serializers.SerializerMethodField()
    phone_number=serializers.SerializerMethodField()

    class Meta():
        model=UserProfile
        fields=['user','phone_number','address']

    def get_user(self,obj):
        return{'username':obj.user.username}
    def get_phone_number(self,obj):
        return{'phone_number':obj.phone_number}
        

class PaymentTransactionsSerializers(serializers.ModelSerializer):

    booking=serializers.SerializerMethodField()
    AmountPaid=serializers.SerializerMethodField()

    class Meta():
        model=PaymentTransactions
        fields=['booking','AmountPaid']
        
    def get_booking(self,obj):
        return{'title':obj.booking.show.movie.title}
    def get_AmountPaid(self,obj):
        return{'AmountPaid':obj.AmountPaid}


