from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "CHROME AI Mentor is online and running 24/7!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
