from .models import Rooms
from utils import *
from django.shortcuts import render
from .forms import LookForFreeForm
from datetime import datetime

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
        f = LookForFreeForm(p_data)
        if f.is_valid:
            # print (f'Тип данных из поля Adults:{type(p_data["adults"])}, значение: {p_data["adults"]}')
            # print (f'Тип данных из поля дата:{type(p_data["type"])}, значение: {p_data["type"] == None}')
            # print (f'Тип данных из поля дата:{type(p_data["date_from"])}, значение: {p_data["date_from"]}')

            room_set = Rooms.objects.all()
            room_set = room_set.filter(adults=int(p_data["adults"])) if p_data["adults"] !='' else room_set
            room_set = room_set.filter(type=int(p_data["type"])) if p_data["type"] !='' else room_set
            
            d_from = datetime.strptime(p_data["date_from"], "%Y-%m-%d")
            d_to = datetime.strptime(p_data["date_to"], "%Y-%m-%d")
            room_set = [r for r in room_set if r.is_free(d_from, d_to)]

            print (f'--------Room set: {room_set}')
            no_rooms = True if len(room_set) == 0 else False

            
        else:
            f = LookForFreeForm()
    else:
        f = LookForFreeForm()
        room_set = Rooms.objects.all()
        no_rooms = False

    title='Search page'
    context={}
    context['menu']          = menu
    context['title']         = title
    context['form']          = f
    context['room_set']      = room_set
    context['no_rooms']      = no_rooms
    return render(request,'user/room_search.html',context)
