# Django admin configuration for the ShortURL model

from django.contrib import admin
from .models import ShortURL

admin.site.register(ShortURL)
# This file registers the ShortURL model with the Django admin site,
