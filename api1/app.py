from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def call_api2():
    try:
        response = requests.get('http://api2:5001')  # เรียก API2 ผ่านชื่อ service ใน docker-compose
        return f'API1 received: {response.text}'
    except Exception as e:
        return f'Error calling API2: {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)