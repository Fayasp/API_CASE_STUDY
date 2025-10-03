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
    return render(request, "weather.html", {"weather": weather_data, "error": error})

def dictionary_lookup(request):
    word = None
    meaning = None
    phonetic = None
    error = None

    if request.method == "POST":
        word = request.POST.get("word")
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url).json()
        print(response)
        print(type(response))

        if isinstance(response, dict) and response.get("title") == "No Definitions Found":
            error = f"No definitions found for '{word}'"
        else:
            try:
                meaning = response[0]["meanings"][0]["definitions"][0]["definition"]
                phonetic = response[0].get("phonetic", "")
            except (KeyError, IndexError):
                error = "Could not parse dictionary response."

    return render(request, "dictionary.html", {
        "word": word,
        "meaning": meaning,
        "phonetic": phonetic,
        "error": error,
    })

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


def get_country_info(request):
    country_info = 0
    country_name= None
    context = {}

    if request.method == "POST":
        country_name = request.POST.get("country")
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url).json()
        print(type(response))

        
        if isinstance(response, dict) and response.get("status") == 404:
            context = {"error": "Country Not Found"}
            return render(request, "country_info.html", status=404, context=context) 
        else:
            context = {

                "name" : response[0]['name']['common'],
                "capital" : response[0]['capital'][0],
                "population" : response[0]['population'],
                "currency": list(response["currencies"].keys())[0] if "currencies" in response else "N/A",
                "region" : response[0]['region'],
                "flag": response[0]['flags']['png']
            }

            return render(request,"country_info.html",context = context)

    return render(request,"country_info.html",context = context)
        
    

def dog_image(request):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    image_url = data['message']
    return render(request, 'dog.html', {'image_url': image_url})