from django.shortcuts import render
from .models import Applicant, Credit

def index(request):
    pass

def applicant_list(request):
    applicants = Applicant.objects.all()
    return render(request, 'creditapp/applicant_list.html', {'applicants': applicants})

def credit_list(request):
    credits = Credit.objects.all()
    return render(request, 'creditapp/credit_list.html', {'credits': credits})
