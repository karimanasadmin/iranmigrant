from django.shortcuts import render
from .models import Taxpayer, TaxSubmission

def taxpayer_list(request):
    taxpayers = Taxpayer.objects.all()
    return render(request, 'taxapp/taxpayer_list.html', {'taxpayers': taxpayers})

def taxsubmission_list(request):
    taxsubmissions = TaxSubmission.objects.all()
    return render(request, 'taxapp/taxsubmission_list.html', {'taxsubmissions': taxsubmissions})
