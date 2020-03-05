from flask import Flask, render_template
from weather import weather_by_city

# initialization our application with name 'server'
app = Flask(__name__)

# use decorator
@app.route('/')
def index():
    title = 'Новости Python'
    weather = weather_by_city('Moscow,Russia')
    return render_template('index.html', page_title=title, weather=weather)


# run our application
if __name__ == '__main__':
    app.run(debug=True)