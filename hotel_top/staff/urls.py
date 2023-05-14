from django.contrib import admin
from django.urls import path, include
from hotel import settings
from django.conf.urls.static import static 
from .views import main_page_staff, inquiries, booking_staff

urlpatterns = [

    path('homepage/', main_page_staff, name='main_page_staff'),
    path('inquiries/', inquiries, name='inquiries'),
    path('bookings/', booking_staff, name='booking_staff'),
]