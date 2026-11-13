import socket

# สร้าง UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ที่อยู่และพอร์ตของ server ที่ต้องการส่งข้อมูลไป
server_address = ("udp_server", 8080)  # แก้ไขให้ตรงกับชื่อ service และพอร์ตใน docker-compose

try:
    # ข้อความที่จะส่งไปยัง server
    message = "Hello from UDP client"

    # แสดงข้อความก่อนการส่ง
    print("Sending message to server...")

    # ส่งข้อความไปยัง server
    client_socket.sendto(message.encode(), server_address)

    # รอรับการตอบกลับจาก server
    response, server = client_socket.recvfrom(1024)
    print(f"Response from server: {response.decode()}")

except Exception as e:
    # แสดงข้อผิดพลาดหากเกิดขึ้น
    print(f"An error occurred: {e}")

finally:
    # ปิด socket
    client_socket.close()
