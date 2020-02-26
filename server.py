from flask import Flask
from weather import weather_by_city

# initialization our application with name 'server'
app = Flask(__name__)

# use decorator
@app.route('/')
def index():
    weather = weather_by_city('Moscow,Russia')
    if weather:
        return f'Погода {weather["temp_C"]}, ощущается как {weather["FeelsLikeC"]}'
    else:
        return 'Сервис погоды временно не доступен'

# run our application
if __name__ == '__main__':
    app.run(debug=True)