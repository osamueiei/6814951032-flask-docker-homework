from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        # แยกพารามิเตอร์จาก URL
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)

        # ตรวจสอบว่ามีพารามิเตอร์ 'msg' หรือไม่
        msg = params.get('msg', ['Hello, World! V2'])[0]  # ค่าเริ่มต้นคือ 'Hello, World!'

        # สร้างการตอบกลับ HTTP
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response = f"<html><body><h1>{msg}</h1></body></html>"
        self.wfile.write(response.encode('utf-8'))

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleServer)
    print("Server running on port 8000...")
    httpd.serve_forever()
