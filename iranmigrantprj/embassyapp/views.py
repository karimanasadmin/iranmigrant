from django.shortcuts import render
from .models import Service, Appointment

def index(request):
    pass

def service_list(request):
    services = Service.objects.all()
    return render(request, 'embassyapp/service_list.html', {'services': services})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'embassyapp/appointment_list.html', {'appointments': appointments})
