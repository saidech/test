import requests
from pprint import pprint

API_Key = 'cb771e45ac79a4e8e2205c0ce66ff633'
#API_Key = '30e91ab40822529e7f8c321cb0ae3697'

city = input("Enter a city ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

# -rev 2.1

pprint(weather_data)