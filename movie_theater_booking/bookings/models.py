

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()    
    duration = models.DurationField(help_text="Duration of the movie (HH:MM:SS)")

#==============================================================================

class Seat(models.Model)        :
    seat_number = models.CharField(max_length = 20)
    is_seat_booked =  models.BooleanField(default = False)
 
#==============================================================================        

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add = True)

    