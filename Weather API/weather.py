from pprint import pprint
from PIL import Image

import requests

API_KEY = '32ad1082216e6f1d77f692b85c1a0175'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    pprint(data)
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)  # In celsius
    print('Weather: ', weather)
    print('Temperature: ', temperature, "C")
else:
    print("Request failed")
