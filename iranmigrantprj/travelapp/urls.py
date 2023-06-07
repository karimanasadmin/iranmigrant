from django.urls import path

from . import views

app_name = 'travelapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.travel_info, name='travel_info'),
    path('book/<int:id>/', views.book_travel, name='book_travel'),
    path('cancel/<int:id>/', views.cancel_booking, name='cancel_booking'),
    path('details/<int:id>/', views.travel_details, name='travel_details'),
    # Add more URL patterns for other views in the travelapp
]
