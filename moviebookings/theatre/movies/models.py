from django.db import models
import uuid



class Movie(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=200,null=True,blank=True)
    director=models.CharField(max_length=200,null=True,blank=True) 
    release_date=models.DateField(null=True,blank=True)
    genre=models.CharField(max_length=300,null=True,blank=True)
    image=models.ImageField(upload_to='profile_pics/',null=True,blank=True)

    def __str__(self):
        return f"{self.title} {self.id}"
                
class Cinema(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    capacity = models.IntegerField(default=150,null=True,blank=True)
    
    def __str__(self):
        return f"{self.name} {self.id}"

class Show(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL,null=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.SET_NULL,null=True)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return f"{self.movie} {self.id}"
    







