import requests

def give_temp(city):
    weather_key ='5c314085f3baa18bdf91b82999484f5b'
    link = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+weather_key

    data = requests.get(link)
    final_data = data.json()
    temp = int(final_data['main']['temp']-273.15)
    return temp

