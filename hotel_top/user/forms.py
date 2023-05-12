from django import forms
from .models import *
from datetime import date, timedelta


class LookForFreeForm(forms.ModelForm):
    date_from = forms.DateField(initial=date.today())
    date_to = forms.DateField(initial=date.today()+timedelta(days=5))
    class Meta:
        model = Rooms
        fields = ['adults', 'type']
        