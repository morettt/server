import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

def check_port(port):
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=2):
            return True
    except:
        return False

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = json.dumps([
            {"服务器名": "内服", "地址": "127.0.0.1:9999", "状态": "在线" if check_port(9999) else "离线"},
            {"服务器名": "外服", "地址": "127.0.0.1:9998", "状态": "在线" if check_port(9998) else "离线"},
        ], ensure_ascii=False)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data.encode())

    def log_message(self, *args):
        pass

print("监控服务运行在 http://127.0.0.1:1000")
HTTPServer(("0.0.0.0", 1000), Handler).serve_forever()
