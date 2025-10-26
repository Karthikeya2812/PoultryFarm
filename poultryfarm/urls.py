"""URL configuration for poultryfarm project."""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def home_view(request):
    return render(request, 'home/index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]

