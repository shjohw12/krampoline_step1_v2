from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import re

def make_class_list():
    class_1 = {"category_id": 1, "class_id": 1, "upload_date": '2025-07-05', "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}             #" "
    class_2 = {"category_id": 1, "class_id": 2, "upload_date": '2025-06-15', "due_date": '2025-06-30', "loc": "서귀포시 성산읍", "now_participants": 5, "max_participants": 8, "how_much": 20000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "여름바다의 맛", "class_article": "바쁜 제주 여성들이 손쉽게 만들어 즐긴 톳냉국을 만들어 더위를 잊어봐요. ", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
    class_3 = {"category_id": 1, "class_id": 3, "upload_date": '2025-07-05', "due_date": '2025-07-19', "loc": "서귀포시 남원읍", "now_participants": 8, "max_participants": 15, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "어부의 보양식", "class_article": "다섯 번만 먹어도 무더위가 사라지는 자리돔 물회를 만들어봐요.", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
    class_4 = {"category_id": 1, "class_id": 4, "upload_date": '2025-05-20', "due_date": '2025-05-28', "loc": "제주시 애월읍", "now_participants": 5, "max_participants": 12, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "시원한 전통해장국", "class_article": "제주에선 각재기로 불리는 전갱이로 담백한 국물맛을 느껴보세요.", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
    class_5 = {"category_id": 1, "class_id": 5, "upload_date": '2025-05-01', "due_date": '2025-05-09', "loc": "제주시 구좌읍", "now_participants": 4, "max_participants": 10, "how_much": 30000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "모래알의 기억", "class_article": "작은 덩치로 오감을 깨우는 황게로와 함께 얼큰한 추억을 만들어요.", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
    class_6 = {"category_id": 1, "class_id": 6, "upload_date": '2025-04-10', "due_date": '2025-04-20', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 5, "how_much": 50000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "베지-근한 맛", "class_article": "소박한 채소와 은빛 갈치가 만난 갈칫국에서 제주의 향기를 발견해보세요.", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
    
    class_list = [class_1, class_2, class_3, class_4, class_5, class_6]
    
    return class_list

def make_category_list():
    category_1 = make_class_list()
    category_2 = []
    category_3 = []
    category_4 = []
    category_5 = []
    category_6 = []
    
    category_list = [category_1, category_2, category_3, category_4, category_5, category_6]
    
    return category_list


def make_applied_list():
    class_list = make_class_list()
    applied_class_list = []
    for x in range(1,3):
        applied_class_list.append(class_list[x-1])
    return applied_class_list
    
    
    
    
'''
class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        for x in make_class_list():
            self.wfile.write(json.dumps(x, ensure_ascii=False).encode('utf-8'))
'''



class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:3000')  
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')  
        self.send_header('Access-Control-Allow-Credentials', 'true')  
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    

    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'message': 'Hello, world!'}
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
        elif re.match(r'^/api/category/\d+$', self.path):
            category_id = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = make_category_list()[int(category_id)-1]
            
            #response = {'category_id': category_id, 'message': 'Category details'}
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
        elif re.match(r'^/api/class/\d+$', self.path):
            class_id = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            for x in make_class_list():
                if x["class_id"] == int(class_id):
                    response = x
                    break
            #response = {'class_id': class_id, 'message': 'class details'}
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8')) 
            
        elif re.match('/api/applied', self.path):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = make_applied_list()
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
        elif re.match('/api/stamp', self.path):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {1:2, 2:0, 3:0, 4:1, 5:0, 6:0}
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
        
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

PORT = 8000

with HTTPServer(("", PORT), CustomHandler) as httpd:
    print(f"서버는 {PORT} 포트에서 실행 중입니다. 종료하려면 Ctrl+C를 누르세요.")
    httpd.serve_forever()