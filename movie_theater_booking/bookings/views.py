from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from .models import Question

permission_classes = [AllowAny]

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')
    return render(request, 'bookings/index.html', {'latest_questions': latest_questions})


# DRF ViewSets
class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]    
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]  # .IsAuthenticatedOrReadOnly] #.AllowAny] #edOrReadOnly]

#==============================================================================
class SeatViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [AllowAny]  #.IsAuthenticatedOrReadOnly]  #.AllowAny]

#==============================================================================
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]
    #permission_classes = [AllowAny]  #.IsAuthenticatedOrReadOnly]  #.AllowAny]

    def create(self, request, *args, **kwargs):
        seat_id = request.data.get('seat')
        movie_id = request.data.get('movie')

        # Check if the seat is already booked for this movie
        if Booking.objects.filter(seat_id=seat_id, movie_id=movie_id).exists():
            return Response(
                {"error": "This seat is already booked for this movie."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)