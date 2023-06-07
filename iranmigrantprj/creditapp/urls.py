from django.urls import path

from . import views

app_name = 'creditapp'

urlpatterns = [
    path('', views.index, name='index'),
    # Add more URL patterns for other views in the creditapp
]
