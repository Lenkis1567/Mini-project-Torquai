"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import main_page, look_for_free, reservation, reviews, InquiryCreate

urlpatterns = [
    path(''       ,      main_page    ,             name = 'main_page_path'),
    path('search/',      look_for_free,             name = 'search_path'),
    path('reservation/', reservation,               name = 'reservation_path'),
    path('review/',      reviews,                   name = 'review_path'),
    path('inquiry/',     InquiryCreate.as_view(),   name = 'inquiry_path'),
    
]
