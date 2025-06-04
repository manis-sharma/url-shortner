from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    path('', include('shortener.urls')),
]


# This file is the main URL configuration for the Django project.
