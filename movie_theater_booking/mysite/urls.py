from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('bookings.urls')),  # root goes to bookings.home
    path('admin/', admin.site.urls),
    path('api/', include('bookings.urls')),  # API endpoints    
]

