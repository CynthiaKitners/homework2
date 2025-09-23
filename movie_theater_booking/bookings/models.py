import os
import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookings.settings")
# django.setup()


from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField() 
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    
    def __str__(self):
        return self.title


class Seats(models.Model):
    seat_number = models.CharField(max_length=10, unique=True)  # e.g., "A1", "B3"
    booking_status = models.BooleanField(default=False)  # True if booked
  
    def __str__(self):
        return f"Seat {self.seat_number} ({'Reserved' if self.is_reserved else 'Available'})"


class Booking(models.Model):
    movie_name = models.CharField(max_length=100)
    seat = models.OneToOneField(  # One seat per booking
        Seat,
        on_delete=models.CASCADE,
        related_name="booking"
    )
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.customer_name} - {self.seat.seat_number}"

        


