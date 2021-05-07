from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return ('<!DOCTYPE html><html lang="en"><head><title>My Flask App</title></head><body><h1>Hello World!!</h1></body></html>')

if __name__ == '__main__':
    # Specifying Port for web application, Default port 5000
    # Starting in debug mode to detect changes in file and restarting the server automatically
    # app.run(port = 7000, debug = True)
    app.run()