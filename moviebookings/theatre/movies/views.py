from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from . response_serializers import *
from .request_serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token

class GetMovieView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data=request.data
        state_name=request.headers.get('naam')
        state_name=self.request.GET.get('sjjj')
        print(state_name)
        movies=Movie.objects.all()
        movies=Movie.objects.filter(director= data['director'])
        movies=Movie.objects.order_by('title')
        movies=Movie.objects.order_by('-title')
        movies=Movie.objects.filter(title__contains='indian 2')
        movies=Movie.objects.filter(title__icontains='Indian 2')
        movies=Movie.objects.filter(title__startswith='The')
        movies=Movie.objects.filter(title__endswith='2')
        serializer=MovieSerializers(movies,many=True).data
        return Response(serializer)
    
class GetCinemaView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data=request.data
        cinemas=Cinema.objects.all()
        cinemas=Cinema.objects.filter(name=data['name'])
        cinemas=Cinema.objects.filter(capacity__gte=1000)
        serializer=CinemaSerializers(cinemas,many=True).data
        return Response(serializer)
    
class GetShowView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data=request.data
        shows=Show.objects.all()
        shows=Show.objects.filter(price__gte=500)
        shows=Show.objects.filter(price__lt=500)
        serializer=ShowSerializers(shows,many=True).data
        return Response(serializer)  

class CreateMovieView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        data=request.data
        movies=Movie.objects.create(tittle=data['title'],director=data['director'],release_date=data['release_[date'],genre=data['genre'],image=data['image'])
        movies.save()
        serializer=MovieSerializers(movies).data
        return Response(serializer)
    
class CreateCinemaView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        Cinemas=Cinema.objects.create(name=data['name'],location=data['location'],capacity=data['capacity'])
        Cinemas.save()
        serializer=CinemaSerializers(Cinemas).data
        return Response(serializer)

class CreateShowView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        movie=Movie.objects.create(title=data['title'])
        cinema=Cinema.objects.create(name=data['name'])
        Shows=Show.objects.create(movie=movie,cinema=cinema,start_time=data['start_time'],end_time=data['end_time'],price=data['price'])
        Shows.save()
        serializer=ShowSerializers(Shows).data
        return Response(serializer)
    
class UpdateMovieView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        movie=Movie.objects.get(id=data["id"])
        if 'id' in data:
            movie.title=data['title']
            movie.save()
            return Response("Movie name update successfully")
        else:
            return Response("Error")


class UpdateCinemaView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        cinema=Cinema.objects.get(id=data['id'])
        if 'id' in data:
            cinema.name=data['name']
            cinema.save()
            return Response('Theatre Name Update Successfully')
        else:
            return Response("Error")
        
class UpdateShowView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        show=Show.objects.get(id=data['id'])
        if 'id' in data:
            show.movie.title=data['title']
            show.movie.save()
            return Response('Show Name Update Successfully')
        else:
            return Response("Error")

class UpdateCreateMovieView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        if 'id' not in data:
            validation=CreateMovieserializers(data=data)
            if validation.is_valid():
                movies=Movie.objects.create(title=data['title'],director=data['director'],release_date=data['release_date'],genre=data['genre'],image=data['image'])
                movies.save()
                return Response('succesfully created')
            else:
                return Response(validation.errors)
        else:
            movie=Movie.objects.get(id=data["id"])
            if 'title' in data:
                movie.title=data['title']
                movie.save()
            if 'director' in data:
                movie.director=data['director']
                movie.save()
            if 'releasedate' in data:
                movie.release_date=['release_date']
                movie.save()
            if 'genre' in data:
                movie.genre=data['genre']
                movie.save()
            if 'image' in data:
                movie.image=data['image']
                movie.save()
            return Response('movie details updated')

class UpdateCreateCinemaView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        if 'id' not in data:
            validation=CreateCinemaserializers(data=data)
            if validation.is_valid():
                Cinemas=Cinema.objects.create(name=data['name'],location=data['location'],capacity=data['capacity'])
                Cinemas.save()
                return Response("created successfully")
            else:
                return Response(validation.errors)
        else:
            cinema=Cinema.objects.get(id=data['id'])
            if 'name' in data:
                cinema.name=data['name']
                cinema.save()
            if 'location' in data:
                cinema.location=data['location']
                cinema.save()
            if 'capacity' in data:
                cinema.capacity=data['capacity']
                cinema.save()
            return Response('cinema details updated')
            
class UpdateCreateShowView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        if 'id' not in data:
            validation=Createshowserializers(data=data)
            if validation.is_valid():
                movie=Movie.objects.create(title=data['title'])
                cinema=Cinema.objects.create(name=data['name'])
                Shows=Show.objects.create(movie=movie,cinema=cinema,start_time=data['start_time'],end_time=data['end_time'],price=data['price'])
                Shows.save()
                return Response('created Successfully')
            else:
                return Response(validation.errors)
        else:
            show=Show.objects.get(id=data['id'])
            if 'title' in data:
                show.movie.title=data['title']
                show.movie.save()
            if 'name' in data:
                show.cinema.name=data['name']
                show.cinema.save()
            if 'start_time' in data:
                show.start_time=data['start_time']
                show.save()
            if 'end_time' in data:
                show.end_time=data['end_time']
                show.save()
            if 'price' in data:
                show.price=data['price']
                show.save()
            return Response('show details updated')
        

class DeleteMovieView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        movies=Movie.objects.get(id=data['id']).delete()
        return Response('Movie Details deleted successfully')

# class DeleteCinemaView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def post(self,request):
#         data=request.data
#         Cinemas=Cinema.objects.get(id=data['id']).delete()
#         return Response('Cinema details deleted successfully') 

class DeleteShowView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data=request.data
        try:
            Shows=Show.objects.get(id=data['id']).delete()
            return Response({'Show details deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'error':'show not found'},status=status.HTTP_404_NOT_FOUND)
        
class RegisterUser(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.create_user(
            username=data['Username'],
            first_name=data['First_name'],
            last_name=data['Last_name'],
            email=data['Email_address'],
            password=data['Password']
        )                   
        token, created = Token.objects.get_or_create(user=user)
        return Response({'successfully created'},status=status.HTTP_201_CREATED)
        

        
from rest_framework.exceptions import NotFound

class DeleteCinemaView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        try:
            # Get the Cinema object with the given ID
            cinema = Cinema.objects.get(id=data['id'])
            cinema.delete()  # Delete the cinema object
            return Response({'message': 'Cinema deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        
        except Cinema.DoesNotExist:
            # Handle the case where the Cinema object with the given ID does not exist
            raise NotFound(detail="Cinema not found")





            




            







    


        
