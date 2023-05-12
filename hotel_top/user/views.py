from utils import *
from django.shortcuts import render

# Create your views here.

def main_page(request):
    on_page_title='Home page'
    context={}
    context['menu']          = menu
    context['on_page_title'] = on_page_title
    return render(request,'user/homepage.html',context)