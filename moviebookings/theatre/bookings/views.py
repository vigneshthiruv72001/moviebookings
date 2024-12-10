from rest_framework.views import  APIView
from rest_framework.response import Response
from . models import *
# from movies.models import *
from . response_serializers import *
from . request_serializers import*
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from twilio.rest import Client





class GetBookingView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        # data=request.data
        Bookings=Booking.objects.all()
        print(Bookings)
        # Bookings=Booking.objects.filter(user=1)
        # Bookings=Booking.objects.filter(total_price__gte=1000)
        # Bookings=Booking.objects.filter(total_price__lt=1000)
        serializer=BookingSerializers(Bookings,many=True).data
        return Response(serializer)
    
class GetUserprofileView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        data=request.data
        userProfile=UserProfile.objects.all()
        serializer=UserprofileSerializers(userProfile,many=True).data
        return Response(serializer)
    
class GetpaymentTransactions(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        data=request.data
        PaymentTransaction=PaymentTransactions.objects.all()
        serializer=PaymentTransactionsSerializers(PaymentTransaction,many=True).data
        return Response(serializer)

class CreateBookingView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        movie=Movie.objects.create(title=data['title'])
        user= User.objects.create(username=data['username'])
        show = Show.objects.create(movie=movie)
        booking = Booking.objects.create(show=show, user=user, quantity=data['quantity'], total_price=(data['total_price']))
        booking.save()
        serializer = BookingSerializers(booking).data
        return Response(serializer)

class CreateUserprofileView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        user=User.objects.create(username=data['username'])
        userProfile=UserProfile.objects.create(user=user , phone_number=data['phone_number'],address=data['address'])
        userProfile.save()
        serializer = UserprofileSerializers(userProfile).data
        return Response(serializer)
    
# class CreatePaymentTransactionsView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]                                               
    # def post(self,request):
    #     data=request.data
    #     movie=Movie.objects.create(title=data['title'])
    #     show=Show.objects.create(movie=movie)
    #     booking=Booking.objects.create(show=show)
    #     paymentTransactions=PaymentTransactions.objects.create(booking=booking,PaymentMethod=data['PaymentMethod'], AmountPaid=data['AmountPaid'],TransactionId=data['TransactionId'])
    #     paymentTransactions.save()
    #     serializer=PaymentTransactionsSerializers(paymentTransactions).data
    #     return Response(serializer)
    
from twilio.rest import Client

class CreatePaymentTransactionsView(APIView):
    def post(self, request):  
        data = request.data
        movie = Movie.objects.create(title=data['title']) 
        show = Show.objects.create(movie=movie)
        booking = Booking.objects.create(show=show)
        payment_transaction = PaymentTransactions.objects.create(
            booking=booking,
            PaymentMethod=data['PaymentMethod'],
            AmountPaid=data['AmountPaid'],
            TransactionId=data['TransactionId']
        )
        payment_transaction.save()
        transaction_id = payment_transaction.id

        TWILIO_ACCOUNT_SID = 'AC574aa144161057e8f02b77f7532bfc3d'
        TWILIO_AUTH_TOKEN = '232928a39a840e4d77d5d56ce0beabee'
        TWILIO_PHONE_NUMBER = '+12562554458'
        recipient_phone_number = data.get('phone', '917558164183')  

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

       
        message = f"Thank you for your payment. Your transaction ID is {transaction_id}. Have a great day!"

     
        try:
            call = client.calls.create(
                to=recipient_phone_number,
                from_=TWILIO_PHONE_NUMBER,
                twiml=f'<Response><Say>{message}</Say></Response>'
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

       
        return Response({
            "payment_transaction_id": transaction_id,
            "twilio_call_sid": call.sid
        }, status=201)
    

class UpdateBookingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        booking=Booking.objects.get(id=data['id'])
        if 'id' in data:
            booking.show.movie.title=data['title']
            booking.show.movie.save()
            booking.user.username=data["username"]
            booking.user.save()
            booking.quantity=data['quantity']
            booking.save()
            booking.total_price=data['total_price']
            booking.save()
            return Response("Movie Name Update Successfully")
        else:
            return Response("Error")
        

class UpdateUserprofileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        userprofile=UserProfile.objects.get(id=data['id'])
        if 'id' in data:
            if 'first_name' in data:
                userprofile.user.first_name = data['first_name']
            if 'last_name' in data:
                userprofile.user.last_name = data['last_name']
                userprofile.user.save()
                userprofile.phone_number=data['phone_number']
                userprofile.save()
                userprofile.address=data['address']
                userprofile.save()
                return Response('Update User_profile details Successfully ')
        else:
            return Response('Error')
        
class UpdatePaymentTransactionsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        paymenttransactions=PaymentTransactions.objects.get(id=data['id'])
        if 'id' in data:
            paymenttransactions.booking.show.movie.title=data['title']
            paymenttransactions.booking.show.movie.save()
            paymenttransactions.PaymentMethod=data['PaymentMethod']
            paymenttransactions.save()
            paymenttransactions.AmountPaid=data['AmountPaid']
            paymenttransactions.save()
            paymenttransactions.TransactionId=data['TransactionId']
            paymenttransactions.save()
            return Response('Updated Payment_transaction details Successfully')
        else:
            return Response('Error')
        
class UpdateCreateBookingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        if 'id' not in data:
            validation=CreateBookingSerializers(data=data)
            if validation.is_valid():
                movie=Movie.objects.create(title=data['title'])
                user= User.objects.create(username=data['username'])
                show = Show.objects.create(movie=movie)
                booking = Booking.objects.create(show=show, user=user, quantity=data['quantity'], total_price=(data['total_price']))
                booking.save()
                return Response('created successfully')
            else:
                return Response(validation.errors)
        else:
            booking=Booking.objects.get(id=data['id'])
            if 'title' in data:
                booking.show.movie.title=data['title']
                booking.show.movie.save()
            if 'username' in data:
                booking.user.username=data['username']
                booking.user.save()
            if 'quantity' in data:
                booking.quantity=data['quantity']
                booking.save()
            if 'total_price' in data:
                booking.total_price=data['total_price']
                booking.save()
            return Response('Booking details updated')
        

class UpdateCreateUserprofileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        if 'id' not in data:
            validation=CreateUserprofileSerializers(data=data)
            if validation.is_valid():
                user=User.objects.create(username=data['username'])
                userProfile=UserProfile.objects.create(user=user , phone_number=data['phone_number'])
                userProfile.save()
                return Response('created succesfully')
            else:
                return Response(validation.errors)
        else:
            userprofile=UserProfile.objects.get(id=data['id'])
            if 'first_name' in data:
                userprofile.user.first_name = data['first_name']
                userprofile.user.save()
            if 'last_name' in data:
                userprofile.user.last_name = data['last_name']
                userprofile.user.save()
            if 'phone_number' in data:
                userprofile.phone_number=data['phone_number']
                userProfile.save()
            if 'address' in data:
                userprofile.address=data['address']
                userprofile.save()
            return Response('userprofile details updated')
        

class UpdateCreatePaymentTransactionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        if 'id' not in data:
            validation=CreatePaymentTransactionsSerializers(data=data)
            if validation.is_valid():
                movie=Movie.objects.create(title=data['title'])
                show=Show.objects.create(movie=movie)
                booking=Booking.objects.create(show=show)
                paymentTransactions=PaymentTransactions.objects.create(booking=booking,PaymentMethod=data['PaymentMethod'], AmountPaid=data['AmountPaid'],TransactionId=data['TransactionId'])
                paymentTransactions.save()
                return Response('Crested Succesfully')
            else:
                return Response(validation.errors)
        else:
            paymenttransactions=PaymentTransactions.objects.get(id=data['id'])

            if 'title' in data:
                paymenttransactions.booking.show.movie.title=data['title']
                paymenttransactions.booking.show.movie.save()

            if 'PaymentMethod' in data:
                paymenttransactions.PaymentMethod=data['PaymentMethod']
                paymenttransactions.save()

            if 'AmountPaid' in data:
                paymenttransactions.AmountPaid=data['AmountPaid']
                paymentTransactions.save()

            if 'TransactionId' in data:
                paymenttransactions.TransactionId=data['TransactionId']
                paymenttransactions.save()

            return Response('updated succesfully')
            


            
