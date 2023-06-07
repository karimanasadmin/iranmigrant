from django.urls import path

from . import views

app_name = 'taxapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.tax_info, name='tax_info'),
    path('submit/', views.submit_tax, name='submit_tax'),
    path('details/<int:id>/', views.tax_details, name='tax_details'),
    path('cancel/<int:id>/', views.cancel_submission, name='cancel_submission'),
    # Add more URL patterns for other views in the taxapp
]
