# Flask Message App (Docker)

เว็บฟอร์มรับข้อความด้วย Flask รันใน Docker และบันทึกทุกข้อความต่อท้ายลงไฟล์ `log.txt` (append mode `"a"`)

## โครงสร้างไฟล์

```
flask-message-app/
├── app.py               # Flask app: ฟอร์ม + บันทึกข้อความลง log.txt แบบ append
├── Dockerfile           # สร้าง image จาก python:3.10-slim
├── requirements.txt     # Flask==2.3.2
├── docker-compose.yml   # service ชื่อ web_app, port 5000, bind mount ./logs
├── logs/log.txt         # ตัวอย่าง log ที่ได้จากการรันจริง
└── README.md
```

## วิธีรัน

```bash
git clone <github-link>
cd flask-message-app
docker-compose up --build -d
```

เปิดเบราว์เซอร์ที่ http://localhost:5000 แล้วพิมพ์ข้อความ กด Submit

## ตรวจสอบ log.txt ใน container

```bash
docker-compose exec web_app cat log.txt
```

ใน container `/app/log.txt` เป็น symlink ไปที่ `/app/logs/log.txt` และไฟล์นี้ bind mount กับ `./logs/log.txt` บนเครื่อง จึงดูไฟล์ได้จากทั้งสองฝั่ง และข้อมูลยังอยู่แม้จะลบ container ไปแล้ว

## ลบเมื่อเสร็จ

```bash
docker-compose down --rmi all
```
