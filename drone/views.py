from django.shortcuts import render
from .models import Flights, Rpas
from .forms import Flightsform

# Create your views here.


def index(request):
    form = Flightsform()
    if request.method == 'POST':
        form = Flightsform(request.POST)
        if form.is_valid():
            try:
                form.save
            except:
                pass
    else:
        form = Flightsform()
    context = {'form':form}
    return render(request, "form.html", context)
    # return render(request, "home.html")

def save_flight(request):
    
    if request.method == 'POST':
        print(response.POST)
        # if response.POST.get('save'):
    pass
        



def flightdata_list(request,reg):
    flights = Flights.objects.filter(rpas__rpas_reg=reg)
    return render(request, "table.html", {'flights':flights})


def flightdata(request):
    # if request.method == 'POST':
    flights = Flights.objects.get(id=id)
    return render(request, "form.html", {'flights':flights})

    
