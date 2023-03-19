from  flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Happy 🥳🥳🥳 ,webhook did it finally,python app'

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port = 8080)
