from django import forms
from django.forms import ModelForm
from .models import Flights

class Flightsform(ModelForm):
    class Meta:
        model = Flights
        fields = '__all__'
        
