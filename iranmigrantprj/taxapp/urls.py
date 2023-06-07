from django.urls import path

from . import views

app_name = 'taxapp'

urlpatterns = [
    path('', views.index, name='index'),
]
