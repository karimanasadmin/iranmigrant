from django.urls import path

from . import views

app_name = 'houseapp'

urlpatterns = [
    path('', views.index, name='index'),
]
