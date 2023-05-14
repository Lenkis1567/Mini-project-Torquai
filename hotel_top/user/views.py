from .models import Rooms, Booking, Review
from utils import *
from django.shortcuts import render, redirect
from .forms import LookForFreeForm, ReservationConfirmationForm, Reviewform
from datetime import datetime
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def main_page(request):
    on_page_title='Home page'
    context={}
    context['menu']          = menu
    context['on_page_title'] = on_page_title
    return render(request,'user/homepage.html',context)

def look_for_free(request):
    if request.method == 'POST':
        p_data = request.POST
        # if p_data.get('search',False):
        f = LookForFreeForm(p_data)
        if f.is_valid:
            # print (f'Тип данных из поля Adults:{type(p_data["adults"])}, значение: {p_data["adults"]}')
            # print (f'Тип данных из поля дата:{type(p_data["type"])}, значение: {p_data["type"] == None}')
            # print (f'Тип данных из поля дата:{type(p_data["date_from"])}, значение: {p_data["date_from"]}')
            date_from = p_data['date_from']
            date_to   = p_data['date_to']
            transit = {'date_from':date_from, 'date_to':date_to}

            room_set = Rooms.objects.all()
            room_set = room_set.filter(adults=int(p_data["adults"])) if p_data["adults"] !='' else room_set
            room_set = room_set.filter(type=int(p_data["type"])) if p_data["type"] !='' else room_set
            
            d_from = datetime.strptime(p_data["date_from"], "%Y-%m-%d")
            d_to = datetime.strptime(p_data["date_to"], "%Y-%m-%d")
            room_set = [r for r in room_set if r.is_free(d_from, d_to)]

            print (f'--------Room set: {room_set}')
            no_rooms = True if len(room_set) == 0 else False
            reservaton = True

        else:
            f = LookForFreeForm()
        # else:
        #     request.session['room_id'] = p_data['reserv']
        #     request.session['date_from'] = p_data['date_from']
        #     request.session['date_to'] = p_data['date_to']
        #     return redirect('reservation_path')
    else:
        f = LookForFreeForm()
        a=f.is_valid()
        date_from = f['date_from'].value().strftime('%Y-%m-%d')
        date_to   = f['date_to'].value().strftime('%Y-%m-%d')
        print (f'-------{type(date_from)}--{date_from}------')
        transit = {'date_from':date_from, 'date_to':date_to}
        room_set = Rooms.objects.all()
        no_rooms = False
        reservaton = False

    title='Search page'
    context={}
    context['menu']          = menu
    context['title']         = title
    context['form']          = f
    context['room_set']      = room_set
    context['transit']       = transit
    context['no_rooms']      = no_rooms
    context['reservaton']    = reservaton
    return render(request,'user/room_search.html',context)


def reservation(request):
    context={}
    if request.method == 'POST':
        p_data=request.POST
        if p_data.get('confirm',False):
            print ('+++++++++++Confirmation reservation',p_data)
            f=ReservationConfirmationForm(request.POST)
            room = Rooms.objects.get(pk=p_data['confirm'])
            date_from = datetime.strptime(p_data["date_from"], "%Y-%m-%d")
            date_to = datetime.strptime(p_data["date_to"], "%Y-%m-%d")
            if f.is_valid:
                name = p_data['name']
                email = p_data['email']
                b = Booking(
                    room           =room, 
                    date_beginning =date_from,
                    date_end       = date_to,
                    name           = name,
                    email          = email,
                    paid           = False
                    )
                b.save()
                messages.success (request,f'Your reservation has been confirmed. The confirmation numder: {b.pk}')
                return redirect('main_page_path')
            else:
                f = ReservationConfirmationForm(request.POST)
                context['room']          = room
                context['room_pk']       = room.pk
                context['date_from']     = date_from.strftime('%Y-%m-%d')
                context['date_to']       = date_to.strftime('%Y-%m-%d')
                context['form']          = f
        else:
            p_data = request.POST
            print(f'+++++ Резервирование {p_data}')
            room = Rooms.objects.get(pk=int(p_data['reserv']))
            print(room)
            date_from = datetime.strptime(p_data["date_from"], "%Y-%m-%d")
            date_to = datetime.strptime(p_data["date_to"], "%Y-%m-%d")
            f = ReservationConfirmationForm()
            context['room']          = room
            context['room_pk']       = room.pk
            context['date_from']     = date_from.strftime('%Y-%m-%d')
            context['date_to']       = date_to.strftime('%Y-%m-%d')
            context['form']          = f
    else:
        context['get'] = True
    title = 'Booking confirmation'
    context['menu']          = menu
    context['title']         = title
    return render(request,'user/reservetion.html',context)

# class ReviewsListView(DataMixin, ListView):
#     model = Review
#     template_name = 'review_list.html' 
#     context_object_name = 'client_reviews'
#     form=Reviewform()
#     context['form'] = form
#     context['menu'] = menu
   
def reviewslistview(request):
    if request.method == 'GET':
        reviews=Review.objects.all()
        reviewform=Reviewform()
        context={"menu":menu, 'client_reviews':reviews, 'form': reviewform}
        return render(request,'user/review_list.html',context)
    if request.method == 'POST':
        new_review=request.POST['reviewbtn']
        print(new_review, request.POST)
        reviews=Review.objects.all()
        context={"menu":menu, 'client_reviews':reviews}
        return render(request,'user/review_list.html',context)