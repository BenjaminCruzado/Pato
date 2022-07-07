import requests
from django.shortcuts import render

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=76b7f8595358b257468ade902701fd35'
    
    city = 'Temuco'

    r = requests.get(url.format(city)).json()
   
    city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'desc' : "",
        }

    print(city_weather)

    if(city_weather['description'] == "overcast clouds"):
        city_weather['desc'] = "Cielo totalmente nublado, recomendamos salir abrigados y con un paraguas por si a caso."
    elif(city_weather['description'] ==  "clear sky"):
        city_weather['desc'] = "Cielo despejado, recomendamos salir con ropa comoda y sin necesidad de llevar un paraguas."
    elif(city_weather['description'] == "few clouds"):
        city_weather['desc'] = "Cielo parcialmente nublado, recomendamos salir un poco abrigados pero sin necesidad de llevar un paraguas."
    elif(city_weather['description'] == "broken clouds"):
        city_weather['desc'] = "Cielo ligeramente nublado, recomendamos salir abrigados y llevar un paraguas."
    elif(city_weather['description'] == "light rain"):
        city_weather['desc'] = "Lluvia ligera, recomendamos salir abrigados, preparados para la lluvia y con un paraguas."
    elif(city_weather['description'] == "heavy rain"):
        city_weather['desc'] = "Lluvia intensa, recomendamos no salir a menos que sea necesario, preparados para la lluvia y con un paraguas."
    elif(city_weather['description'] == "rain"):
        city_weather['desc'] = "Lluvia, recomendamos salir preparados para la lluvia y con un paraguas."
    elif(city_weather['description'] == "scattered clouds"):
        city_weather['desc'] = "Nubes dispersas, recomendamos salir abrigados para el frio y si desea ser cauteloso salir con un paraguas."






    context = {'clima_ciudad' : city_weather}


    return render(request, 'clima/clima.html', context)
