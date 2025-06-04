# This file is part of a URL shortener application.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
]
# This file defines the URL patterns for the shortener application.