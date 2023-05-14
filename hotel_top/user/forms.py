from os import name
from django import forms
from .models import *
from datetime import date, timedelta
from datetime import datetime


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
        
    def clean_date_from(self):
        date = self.cleaned_data.get('date_from')
        print (f"date:{date}, type: {type(date)}, datetime.today() {type(datetime.today().date())}")
        # date = datetime.strptime(date["date_from"], "%Y-%m-%d")
        if date < datetime.today().date():
            print ('The start date cannot be less than the current one')
            raise forms.ValidationError("The start date cannot be less than the current one")
        return date

    def clean(self):
        c_date = super().clean()
        date_from = c_date['date_from']
        date_to = c_date['date_to']
        print (f"date:{date_from}, type: {type(date_from)}, datetime.today() ")
        # date = datetime.strptime(date["date_from"], "%Y-%m-%d")
        if date_to < date_from:
            print ('The finish date cannot be less than start date')
            raise forms.ValidationError("The finish date cannot be less than start date")
        if (date_to - date_from).days < 2:
            print ('The rental period cannot be less than two days')
            raise forms.ValidationError("The rental period cannot be less than two days")
        if (date_to - date_from).days > 20:
            print ('The rental period cannot be more than twenty days')
            raise forms.ValidationError("The rental period cannot be more than twenty days")

        return c_date

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


class Reviewform(forms.Form):
    text = forms.CharField(max_length=100, label="Write what you think aout staying in the hotel")
    email = forms.EmailField( label="Enter your e-mail")

class InquiryForm(models.Form):
        class Meta:
            model = Inquiry
            fields = ['text', 'email']
            

