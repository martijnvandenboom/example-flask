from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! My name is Martijn van den Boom.'


if __name__ == "__main__":
    app.run()
