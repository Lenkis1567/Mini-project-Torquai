from .models import Rooms
from utils import *
from django.shortcuts import render
from .forms import LookForFreeForm

# Create your views here.

def main_page(request):
    on_page_title='Home page'
    context={}
    context['menu']          = menu
    context['on_page_title'] = on_page_title
    return render(request,'user/homepage.html',context)

def look_for_free(request):

    f = LookForFreeForm()
    title='Search page'
    room_set = Rooms.objects.all()
    for r in room_set:
        print (r.r_photo.all().filter(main_photo=True))
    context={}
    context['menu']          = menu
    context['title'] = title
    context['form'] = f
    context['room_set']=room_set
    return render(request,'user/room_search.html',context)
