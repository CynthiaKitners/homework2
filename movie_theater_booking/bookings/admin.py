# Register your models here.
from django.contrib import admin
from .models import Movie, Seat, Booking, Question
from .models import Question

admin.site.register(Question)

admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Booking)









