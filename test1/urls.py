from django.urls import path
from .views import dog_image,weather_view,get_quotes

urlpatterns = [
    path('', dog_image, name='dog_image'),
    path("weather/", weather_view, name="weather"),
    path("quotes/", get_quotes, name="get_quotes"),
]




