from django.urls import path
from . import views

urlpatterns=[
    path('getMovieView', views.GetMovieView.as_view(), name='getMovieview'),
    path('getCinemaView',views.GetCinemaView.as_view(),name='getCinemaView'),
    path('getShowView',views.GetShowView.as_view(),name='getShowView'),
    path('CreateMovieView',views.CreateMovieView.as_view(),name='CreateMovieView'),
    path('CreateCinemaView',views.CreateCinemaView.as_view(),name='CreteCinemaView'),
    path('CreateShowView',views.CreateShowView.as_view(),name='CreateShowView'),
    path('updateMovieView',views.UpdateMovieView.as_view(),name='updateMovieView'),
    path('updateCinemaView',views.UpdateCinemaView.as_view(),name='updateCinemaView'),
    path('updateShowView',views.UpdateShowView.as_view(),name='updateShowView'),
    path('updateCreateMovieView',views.UpdateCreateMovieView.as_view(),name='updateCreateMovieView'),
    path('updateCreateCinemaView',views.UpdateCreateCinemaView.as_view(),name='updateCreateCinemaView'),
    path('updateCreateShowView',views.UpdateCreateShowView.as_view(),name='updateCreateShowView'),
    path('deleteMovieView',views.DeleteMovieView.as_view(),name='deleteMovieView'),
    path('deleteCinemaView',views.DeleteCinemaView.as_view(),name='deleteCinemaView'),
    path('deleteShowView',views.DeleteShowView.as_view(),name='deleteShowView'),
    path('registeruser', views.RegisterUser.as_view(),name='registeruser')
]