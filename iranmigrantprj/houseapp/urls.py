from django.urls import path

from . import views

app_name = 'houseapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('listings/', views.house_listings, name='house_listings'),
    path('details/<int:id>/', views.house_details, name='house_details'),
    path('rent/<int:id>/', views.rent_house, name='rent_house'),
    path('cancel/<int:id>/', views.cancel_rental, name='cancel_rental'),
    # Add more URL patterns for other views in the houseapp
]
