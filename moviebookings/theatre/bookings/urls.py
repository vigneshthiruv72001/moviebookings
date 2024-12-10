from django.urls import path
from . import views

urlpatterns=[
    path('getBookingView',views.GetBookingView.as_view(),name='getBookingView'),
    path('getUserprofileView',views.GetUserprofileView.as_view(),name='getUserprofileView'),
    path('getpaymentTransaction',views.GetpaymentTransactions.as_view(),name='getpaymentTransaction'),
    path('createBookingView',views.CreateBookingView.as_view(),name='createBookingView'),
    path('createuserprofileView',views.CreateUserprofileView.as_view(),name='createuserprofileView'),
    path('createPaymentTransactionsView',views.CreatePaymentTransactionsView.as_view(),name='createPaymentTransactionsView'),
    path('updateBookingView',views.UpdateBookingView.as_view(),name='updateBookingView'),
    path('updateUserProfileView',views.UpdateUserprofileView.as_view(),name='updateUserProfileView'),
    path('updatePaymentTransactionsView',views.UpdatePaymentTransactionsView.as_view(),name='updatePaymentTransactionsView'),
    path('updateCreateBookingView',views.UpdateCreateBookingView.as_view(),name='updateCreateBookingView'),
    path('updateCreateUserProfileView',views.UpdateCreateUserprofileView.as_view(),name='updateCreateUserProfileView'),  
]

