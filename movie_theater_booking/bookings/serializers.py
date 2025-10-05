from rest_framework import serializers
from .models import Movie, Seat, Booking
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class MyViewSet(viewsets.ViewSet):
    def list(self, request):  # handles GET
        return Response({"message": "GET request"})

    def create(self, request):  # handles POST
        data = request.data
        return Response({"received": data})


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_date']  # list your fields here

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
