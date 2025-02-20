from http.server import SimpleHTTPRequestHandler, HTTPServer
import json


class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()

        data = {
            "message": "Hello krampoline!",
            "status": "success"
        }
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))


PORT = 3000

with HTTPServer(("", PORT), CustomHandler) as httpd:
    print(f"서버는 {PORT} 포트에서 실행 중입니다. 종료하려면 Ctrl+C를 누르세요.")
    httpd.serve_forever()
