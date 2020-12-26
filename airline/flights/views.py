from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flights,Airport, Passenger


# Create your views here.
# def index(request):
#     return()

def index(request):
    return render(request,"layouts/index.html",{
        "flights": Flights.objects.all()
    })
def flight(request,flight_id):
    flight = Flights.objects.get(pk=flight_id)
    return render(request,"layouts/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_pass": Passenger.objects.exclude(id=flight_id).all()
    })
def book(request,flight_id):
    
    if request.method == "POST":
        flight = Flights.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
    return HttpResponseRedirect("flights",args=(flight.id,))
