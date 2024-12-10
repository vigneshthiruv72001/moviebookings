from rest_framework import serializers
from . models import*

class CreateMovieserializers(serializers.Serializer):
    title=serializers.CharField(max_length=200)
    director=serializers.CharField(max_length=200)
    release_date=serializers.DateField()
    genre=serializers.CharField(max_length=300)

class CreateCinemaserializers(serializers.Serializer):
    name=serializers.CharField(max_length=225)
    location=serializers.CharField(max_length=225)
    capacity=serializers.IntegerField()

class Createshowserializers(serializers.Serializer):
    start_time=serializers.DateTimeField()
    end_time=serializers.DateTimeField()
    price=serializers.DecimalField(max_digits=10,decimal_places=2)
    

