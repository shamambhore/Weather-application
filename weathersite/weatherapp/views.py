import imp
from django.shortcuts import render
import urllib.request
import json
import requests

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        appid = '2d65a6bbce9d00a20ffb8bff137b8e71'
        URL ='https://api.openweathermap.org/data/2.5/weather'
        PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
        req = requests.get(url=URL, params=PARAMS)
        # source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=akola&appid=2d65a6bbce9d00a20ffb8bff137b8e71").read()
        list_of_data = req.json()
        
        weather_data ={
            'country_code':str(list_of_data['sys']['country']),
            'Lon':str(list_of_data['coord']['lon']),
            'Lat':str(list_of_data['coord']['lat']),
            'temp':str(list_of_data['main']['temp']) + ' degree/C',
            'pressure':str(list_of_data['main']['pressure']),
            'humidity':str(list_of_data['main']['humidity']),
            'main':str(list_of_data['weather'][0]['main']),
            'description':str(list_of_data['weather'][0]['description']),
            'icon':list_of_data['weather'][0]['icon'],
        }
        # print(weather_data)
    else:
        weather_data={}
        
        
    return render(request, 'index.html', weather_data)
