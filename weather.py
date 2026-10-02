
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city='Sofia'):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Weather App ***')
    city = input("Enter a city name: ")

    if not bool(city.strip()):
        city = "Burgas"
        
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
    
#     {'base': 'stations',
#  'clouds': {'all': 76},
#  'cod': 200,
#  'coord': {'lat': 42.6975, 'lon': 23.3242},
#  'dt': 1790947582,
#  'id': 727011,
#  'main': {'feels_like': 16.17,
#           'grnd_level': 965,
#           'humidity': 36,
#           'pressure': 1031,
#           'sea_level': 1031,
#           'temp': 17.43,
#           'temp_max': 18.83,
#           'temp_min': 17.34},
#  'name': 'Sofia',
#  'sys': {'country': 'BG',
#          'id': 2113241,
#          'sunrise': 1790915071,
#          'sunset': 1790957254,
#          'type': 2},
#  'timezone': 10800,
#  'visibility': 10000,
#  'weather': [{'description': 'broken clouds',
#               'icon': '04d',
#               'id': 803,
#               'main': 'Clouds'}],
#  'wind': {'deg': 30, 'speed': 5.66}}