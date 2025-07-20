# my-docker-api
https://github.com/Phasiya/my-docker-api
โครงสร้างโปรเจกต์

my-docker-api/
         api1/
│    app.py
│    Dockerfile
├       api2/
│    app.py
│    Dockerfile
docker-compose.yml
-README.md


---

-โค้ด API แต่ละตัว

✅ api1/app.py

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def call_api2():
    try:
        response = requests.get('http://api2:5001')  # เรียก API2 ผ่านชื่อ service
        return f'API1 received: {response.text}'
    except Exception as e:
        return f'Error calling API2: {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

✅ api2/app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from API 2!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


---

-Dockerfile (เหมือนกันทั้ง api1 และ api2)

ชื่อไฟล์: Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install flask requests

CMD ["python", "app.py"]


---

-docker-compose.yml

version: '3'
services:
  api1:
    build: ./api1
    ports:
      - "5000:5000"
  api2:
    build: ./api2
    ports:
      - "5001:5001"


---

-สั่งรันโปรเจกต์ด้วย Docker Compose

เปิด CMD แล้วรันคำสั่ง:

cd C:\Users\ASUS\my-docker-api
docker compose up --build


ทดสอบ API บนเบราว์เซอร์

เข้า http://localhost:5000 ➜ API1 จะเรียก API2 และแสดงผลว่า
API1 received: Hello from API 2!



-อัปโหลด GitHub

คำสั่ง:

git init
git remote add origin https://github.com/Phasiya/my-docker-api.git
git add .
git commit -m "Add API1, API2, Dockerfile, and docker-compose"
git push origin main




-เขียน README.md (ตัวอย่างง่ายๆ)

# my-docker-api

โปรเจกต์นี้สร้าง API 2 ตัวที่เชื่อมต่อกันด้วย Docker Compose

## วิธีใช้งาน

1. สั่งรัน:
```bash
docker compose up --build

2. เปิดเบราว์เซอร์ไปที่:



http://localhost:5000
