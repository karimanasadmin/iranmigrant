from django.shortcuts import render
from .models import Destination, Travel

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'travelapp/destination_list.html', {'destinations': destinations})

def travel_list(request):
    travels = Travel.objects.all()
    return render(request, 'travelapp/travel_list.html', {'travels': travels})
