import requests
import json
from datetime import datetime
from Ex12_apikey import open_weather_key
#Module12
#Exercise1
server= "https://api.chucknorris.io"
request= server + "/jokes/random"
try:
    response = requests.get(request).json()
    #print(json.dumps(response, indent=2))
    print(response["value"])
except requests.exceptions.RequestException as e:
    print("Request failed")

#Exercise2
def open_weathermap(city):
    sver= "https://api.openweathermap.org"
    req= sver + "/data/2.5/weather" + "?q=" + city + "&appid=" + open_weather_key()
    response= requests.get(req)
    return response.status_code, requests.get(req).json()
def temp_in_cel(kelvin):
    return kelvin - 273.15

city= input("Enter a city name to check the weather: ")
try:
    (result,data)= open_weathermap(city)
    if result==200:
        print(f"Current weather: {data["weather"][0]["description"]}")
        print(f"Temperature: {temp_in_cel(data["main"]["temp"])} C")
    elif result==401:
        print("Not a valid API key.")
    elif result==404:
        print(f"No weather data found for {city}")
    else:
        print(f"Unknown response code: str{result}")
except requests.exceptions.RequestException as e:
    print("Request failed")