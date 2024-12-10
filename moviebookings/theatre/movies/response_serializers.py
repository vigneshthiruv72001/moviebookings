from rest_framework import serializers
from. models import*
from django.contrib.auth.models import User

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['tittle','director','release_date','genre','image']

class CinemaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Cinema
        fields=['name','location','capacity']

class ShowSerializers(serializers.ModelSerializer):
    movie=serializers.SerializerMethodField()
    cinema=serializers.SerializerMethodField()
    class Meta:
        model=Show
        fields=['movie','cinema','start_time','end_time','price']
    def get_movie(self,obj):
        return{'tittle':obj.movie.title}
    def get_cinema(self,obj):
        return{'name':obj.cinema.name}
    
