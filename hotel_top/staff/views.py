from django.shortcuts import render, redirect
from utils import *
from user.models import *

# Create your views here.
def main_page_staff(request):
    # permission_classes = (IsStaff, )
    on_page_title='Home page'
    context={}
    context['menu']          = menu
    context['on_page_title'] = on_page_title
    return render(request,'staff/homepage.html',context) 

def inquiries(request):
    if request.method =="GET":
        inq = Inquiry.objects.all()
        context={"inquiries": inq}
    if request.method=="POST":
        print(request, request.POST['mybtn'])
        inq_id=int(request.POST['mybtn'])
        inq=Inquiry.objects.get(pk=inq_id)
        inq.is_answered=True
        inq.save()
        inq1= Inquiry.objects.all()
        context={"inquiries": inq1}

    return render(request,'staff/inquiries.html', context) 

def booking_staff(request):
    if request.method =="GET":
        bookings_list=Booking.objects.all()
        context={'bookings': bookings_list}

    if request.method=="POST":
        print(request, request.POST['cancel'])
        booking_id=int(request.POST['cancel'])
        book=Booking.objects.get(pk=booking_id)
        book.canceled =True
        book.save()
        booking_list1= Booking.objects.all()
        context={"bookings": booking_list1}

    return render(request,'staff/bookings.html', context) 