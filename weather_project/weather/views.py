from django.shortcuts import render

from .models import SearchHistory
import requests

API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def weather_view(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        if response.status_code == 200:
            weather_data = response.json()
            SearchHistory.objects.create(city=city)
    return render(request, 'weather/weather.html', {'weather_data': weather_data})

# Create your views here.
