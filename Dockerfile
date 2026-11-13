# ใช้ Python image
FROM python:3.10-slim

# กำหนดโฟลเดอร์การทำงาน
WORKDIR /app

# คัดลอกไฟล์โค้ดไปยัง container
COPY app.py .

# รันโค้ด Python
CMD ["python", "app.py"]