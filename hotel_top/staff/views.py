from django.http import HttpResponse
from django.shortcuts import render, redirect
from utils import *
from user.models import *
from django.contrib.auth.decorators import login_required #Dima
from django.http import HttpResponseForbidden #Dima
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


@login_required 
def main_page_staff(request):
    if not request.user.is_staff: 
        return HttpResponseForbidden ('Access is denied') 
    on_page_title='Home page'
    context={}
    context['menu']          = staff_menu #Dima
    context['on_page_title'] = on_page_title
    return render(request,'staff/homepage.html',context) 



@login_required 
def inquiries(request):
    if not request.user.is_staff: 
        return HttpResponseForbidden ('Access is denied') 
    if request.method =="GET":
        inq = Inquiry.objects.all()
        context={"inquiries": inq}
        context['menu']          = staff_menu #Dima
    if request.method=="POST":
        print(request, request.POST['mybtn'])
        inq_id=int(request.POST['mybtn'])
        inq=Inquiry.objects.get(pk=inq_id)
        inq.is_answered=True
        inq.save()
        inq1= Inquiry.objects.all()
        context={"inquiries": inq1}
        context['menu']          = staff_menu #Dima

    return render(request,'staff/inquiries.html', context) 

@login_required
def booking_staff(request):
    if not request.user.is_staff: 
        return HttpResponseForbidden ('Access is denied')
    if request.method =="GET":
        bookings_list=Booking.objects.all()
        context={'bookings': bookings_list}
        context['menu']          = staff_menu #Dima

    if request.method=="POST":
        print(request, request.POST['cancel'])
        booking_id=int(request.POST['cancel'])
        book=Booking.objects.get(pk=booking_id)
        book.canceled =True
        book.save()
        booking_list1= Booking.objects.all()
        context={"bookings": booking_list1}
        context['menu']          = staff_menu #Dima

    return render(request,'staff/bookings.html', context) 

class ReviewsStaffListView(DataMixin, ListView):
    model = Review
    template_name = 'staff/reviews.html' 
    context_object_name = 'reviews'
    

class ReviewDeleteView(DataMixin, DeleteView):
    model = Review
    template_name = 'staff/reviews.html'
    success_url = reverse_lazy('reviews_staff')