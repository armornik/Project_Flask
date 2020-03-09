import requests
from webapp.params_weather import key_id, weather_url



def weather_by_city(city_name):
    params = {
        'key': key_id,
        'q': city_name,
        'format': 'json',
        'num_of_days': '1',
        'lang': 'ru'
    }

    try:
        result = requests.get(weather_url, params=params)
        # Обработка 400 и 500 ошибок
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False

if __name__ == "__main__":
    print(weather_by_city('Moscow,Russia'))