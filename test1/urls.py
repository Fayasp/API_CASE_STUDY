from django.urls import path
from .views import dog_image,weather_view,get_quotes,dictionary_lookup,get_country_info

urlpatterns = [
    path('', dog_image, name='dog_image'),
    path("weather/", weather_view, name="weather"),
    path("quotes/", get_quotes, name="get_quotes"),
    path("dictionary/",dictionary_lookup,name="dictionary_lookup"),
    path("country/",get_country_info,name="get_country_info")
]




