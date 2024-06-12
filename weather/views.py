from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

def index(request):
    return render(request, 'weather/index.html')


def get_weather(request, city_name):
    api_key = "b1fd6e14799699504191b6bdbcadfc35"  
    unit = "metric"
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={unit}"

    response = requests.get(api_url)
    data = response.json()

    if data.get('cod') != 404:
        weather_data = {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "weatherType": data["weather"][0]["description"],
            "realFeel": data["main"]["feels_like"],
            "windSpeed": data["wind"]["speed"],
            "windDirection": data["wind"]["deg"],
            "visibility": data["visibility"] / 1000,
            "pressure": data["main"]["pressure"],
            "maxTemperature": data["main"]["temp_max"],
            "minTemperature": data["main"]["temp_min"],
            "humidity": data["main"]["humidity"],
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"],
        }
    else:
        weather_data = {"message": "city not found"}

    return JsonResponse(weather_data)
