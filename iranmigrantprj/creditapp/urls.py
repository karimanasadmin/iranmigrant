from django.urls import path

from . import views

app_name = 'creditapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.apply_credit, name='apply_credit'),
    path('history/', views.credit_history, name='credit_history'),
    path('details/<int:id>/', views.credit_details, name='credit_details'),
    path('approve/<int:id>/', views.approve_credit, name='approve_credit'),
    path('reject/<int:id>/', views.reject_credit, name='reject_credit'),
    # Add more URL patterns for other views in the creditapp
]
