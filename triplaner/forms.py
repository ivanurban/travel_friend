from django import forms

from .models import Trip, Destination, Flight, Hotel

from django.contrib.auth.models import User 

# class TripAddForm(forms.Form):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = forms.CharField()
#     slug = forms.SlugField() 
#     start_date = forms.DateTimeField()

#using modal form to save new trip in database
class TripAddModelForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'start_date']

class DestinationAddModelForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['location']


class FlightAddModelForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['from_destination','destination','date_time','price']
    


class HotelAddModelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'price','check_in_date','check_out_date']