from django.shortcuts import render
from .models import Flights, Rpas
from .forms import Flightsform

# Create your views here.


def index(request):
    return render(request, "home.html")
    

def addflight(request):
    form = Flightsform()
    if request.method == 'POST':
        form = Flightsform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = Flightsform()
    context = {'form':form}
    return render(request, "form.html", context)
    

def rpasflights(request,reg):
    flights = Flights.objects.filter(rpas__rpas_reg=reg)
    return render(request, "table.html", {'flights':flights})


    
