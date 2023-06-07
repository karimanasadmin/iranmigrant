from django.shortcuts import render
from .models import Address, House

def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'houseapp/address_list.html', {'addresses': addresses})

def house_list(request):
    houses = House.objects.all()
    return render(request, 'houseapp/house_list.html', {'houses': houses})
