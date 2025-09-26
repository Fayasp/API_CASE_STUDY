from django.shortcuts import render

import requests
from django.conf import settings



# api_key = settings.API_KEY



def weather_view(request):
    weather_data = None
    error = None


    api_key = settings.API_KEY

    if request.method == "POST":
        city = request.POST.get("city")
       
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


        response = requests.get(url).json()
        print(response)

        if response.get("cod") != 200:
            error = response.get("message", "Error fetching data")
        else:
            weather_data = {
                "city": response["name"],
                "temp": response["main"]["temp"],
                "description": response["weather"][0]["description"],
                "icon": response["weather"][0]["icon"],
                "main": response["weather"][0]["main"],  # for background
            }
        print(weather_data)

    return render(request, "weather.html", {"weather": weather_data, "error": error})



def get_quotes(request):
    
    
    api_key = settings.API_KEY

    url = 'https://api.api-ninjas.com/v1/quotes'
    headers = {'X-Api-Key': api_key}
    response = requests.get(url,headers)
    data = response.json()
    quote_data = {
        "quotes" :  data[0]['quote'],
        'author' :  data[0]['author']
    }
    print(quote_data)

    return render(request,'quotes.html',{"quote_data":quote_data})

def dog_image(request):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    image_url = data['message']
    return render(request, 'dog.html', {'image_url': image_url})