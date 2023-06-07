from django.shortcuts import render
from .models import Hobby


def index(request):
    pass


def hobby_list(request):
    hobbies = Hobby.objects.all()
    return render(request, 'hobbiesapp/hobby_list.html', {'hobbies': hobbies})
