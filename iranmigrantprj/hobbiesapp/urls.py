from django.urls import path

from . import views

app_name = 'hobbiesapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('interests/', views.hobbies_interests, name='hobbies_interests'),
    path('add/', views.add_hobby, name='add_hobby'),
    path('edit/<int:id>/', views.edit_hobby, name='edit_hobby'),
    path('delete/<int:id>/', views.delete_hobby, name='delete_hobby'),
    # Add more URL patterns for other views in the hobbiesapp
]
