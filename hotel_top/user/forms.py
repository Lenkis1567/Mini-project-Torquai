from django import forms
from .models import *
from datetime import date, timedelta


class LookForFreeForm(forms.ModelForm):
    date_from = forms.DateField(initial=date.today(),
                                widget=forms.DateInput(attrs={'type': 'date'})
                                )
    date_to = forms.DateField(initial=date.today()+timedelta(days=5),
                                widget=forms.DateInput(attrs={'type': 'date'})
                                )
    adults = forms.ModelChoiceField (AdultsCount.objects.all(), required=False)
    type   = forms.ModelChoiceField (RoomType.objects.all(), required=False)
    class Meta:
        model = Rooms
        fields = ['adults', 'type']
        