from django.urls import path

from . import views

app_name = 'embassyapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.embassy_services, name='embassy_services'),
    path('appointment/', views.book_appointment, name='book_appointment'),
    path('details/<int:id>/', views.appointment_details, name='appointment_details'),
    path('cancel/<int:id>/', views.cancel_appointment, name='cancel_appointment'),
    # Add more URL patterns for other views in the embassyapp
]
