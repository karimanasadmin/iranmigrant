from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('credit/', include('creditapp.urls')),
    path('travel/', include('travelapp.urls')),
    path('embassy/', include('embassyapp.urls')),
    path('house/', include('houseapp.urls')),
    path('tax/', include('taxapp.urls')),
    path('hobbies/', include('hobbiesapp.urls')),
    path('', views.index, name='home'),
]
