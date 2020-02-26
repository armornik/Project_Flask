import requests
from params_weather import params

def weather_by_city(city_name):
    weather_url = 'https://api.worldweatheronline.com/premium/v1/weather.ashx'

    result = requests.get(weather_url, params=params(city_name))
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False

if __name__ == "__main__":
    print(weather_by_city('Moscow,Russia'))