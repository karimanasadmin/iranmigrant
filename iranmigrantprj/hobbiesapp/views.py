from django.shortcuts import render
from .models import Hobby

def hobby_list(request):
    hobbies = Hobby.objects.all()
    return render(request, 'hobbiesapp/hobby_list.html', {'hobbies': hobbies})
