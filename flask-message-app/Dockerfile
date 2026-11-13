FROM python:3.10-slim

WORKDIR /app

# ติดตั้ง dependencies ก่อน เพื่อให้ Docker cache layer นี้ได้
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# ทำ symlink /app/log.txt -> /app/logs/log.txt
# เพื่อให้คำสั่ง `docker-compose exec web_app cat log.txt` อ่านไฟล์ log ได้ตรง ๆ
RUN mkdir -p /app/logs && ln -s /app/logs/log.txt /app/log.txt

ENV PYTHONUNBUFFERED=1
EXPOSE 5000

CMD ["python", "app.py"]
