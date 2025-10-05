import datetime
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone

# bookings/migrations/000X_add_text_to_question.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('bookings', 'previous_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
    ]

# bookings/views.py
from django.shortcuts import render
#from .models import Question

def index(request):
    # Get the 5 most recent questions by creation time
    latest_questions = Question.objects.order_by('-created_at')[:5]
    
    context = {
        'latest_questions': latest_questions
    }
    
    return render(request, 'bookings/index.html', context)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.movie.title} - Seat {self.seat_number}"

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="bookings")
    user_name = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} booked {self.seats} seats for {self.movie.title}"

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'  # optional: allow sorting
    was_published_recently.boolean = True                  # optional: show as True/False icon
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Link each choice to a question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
    def __str__(self):
        return self.text


    def was_published_recently(self):
         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
   