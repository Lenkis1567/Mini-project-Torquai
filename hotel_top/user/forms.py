from os import name
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
        
class ReservationConfirmationForm (forms.Form):
    name  = forms.CharField(max_length=100,
                            label="Enter your first and last name",
                            error_messages={
                                'required':"This field is required",
                                'error_messages':"Error in filling"
														}
                            )
    email = forms.EmailField(
                            label="Enter your e-mail",
                            error_messages={
                                'required':"This field is required",
                                'error_messages':"Error in filling"
														}
                            )
        