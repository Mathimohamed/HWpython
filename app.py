from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome Mathi Mohamed Hi mathi mohamed'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
