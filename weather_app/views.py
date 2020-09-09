from django.http import HttpResponse
from django.shortcuts import render
import requests
import os
from . import forms

# Create your views here.


city_list = []

def search(request):
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        if search_form.is_valid():
            city = search_form.cleaned_data['search_city']
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
            api_key = os.environ.get('DJ_WEATHER_APP')
            #API calling
            api_data = requests.get(url.format(city,api_key)).json()
            # print(r.text)
            city_weather = {
                'name': city,
                'temperature': api_data['main']['temp'],
                'description': api_data['weather'][0]['description'],
                'icon': api_data['weather'][0]['icon']
            }
            search_form = forms.SearchForm()
            return render(request, 'weather_app/index.html', {'city_weather': city_weather, 'form': search_form})
        else:
            return HttpResponse('form error!')
    else:
        search_form = forms.SearchForm()
        city = 'Mumbai' #default city
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        api_key = os.environ.get('DJ_WEATHER_APP')
        api_data = requests.get(url.format(city,api_key)).json()
        city_weather = {
            'name': city,
            'temperature': api_data['main']['temp'],
            'description': api_data['weather'][0]['description'],
            'icon': api_data['weather'][0]['icon']
        }
        return render(request, 'weather_app/index.html', {'city_weather': city_weather, 'form': search_form})


def multiple_weather(request):
    if request.method == 'POST':
        adding_city = forms.AddCity(request.POST)
        if adding_city.is_valid():
            city = adding_city.cleaned_data['add_city']
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
            api_key = os.environ.get('DJ_WEATHER_APP')
            api_data = requests.get(url.format(city,api_key)).json()
            city_list.append(api_data)
            # print(r.text)
            # print(city_list)
            #converting temperature from K to C.
            api_data['main']['temp'] = round(api_data['main']['temp']) - 273
            adding_city = forms.AddCity()
            return render(request, 'weather_app/multiple.html', {'city_list': city_list, 'adding_city': adding_city})

    else:
        city_list.clear()
        adding_city = forms.AddCity()
        return render(request, 'weather_app/multiple.html', {'adding_city': adding_city})
