from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
import random, string

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def home(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_code = generate_short_code()
        while ShortURL.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code()
        short_url = ShortURL.objects.create(original_url=original_url, short_code=short_code)
        return render(request, 'shortener/home.html', {'short_url': short_url})
    return render(request, 'shortener/home.html')

def redirect_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(short_url.original_url)
# This file contains the views for the URL shortener application.