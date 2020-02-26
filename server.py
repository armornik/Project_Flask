from flask import Flask

# initialization our application with name 'server'
app = Flask(__name__)

# use decorator
@app.route('/')
def index():
    return 'Hi Flask!'

# run our application
if __name__ == '__main__':
    app.run()