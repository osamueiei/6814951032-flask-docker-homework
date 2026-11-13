import socket

# สร้าง socket สำหรับ server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server is starting...")
server_socket.bind(("0.0.0.0", 8080))  # ใช้พอร์ต 8080
print("UDP server is up and listening...")

try:
    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f"Message from {client_address}: {message.decode()}")
        server_socket.sendto(b"Received your message!", client_address)
except KeyboardInterrupt:
    print("Server is shutting down.")
finally:
    server_socket.close()