class_1 = {"category": "바다의 기억", "class_id": 1, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}             #" "
class_2 = {"category": "바다의 기억", "class_id": 2, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
class_3 = {"category": "바다의 기억", "class_id": 3, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
class_4 = {"category": "바다의 기억", "class_id": 4, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
class_5 = {"category": "바다의 기억", "class_id": 5, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
class_6 = {"category": "바다의 기억", "class_id": 6, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
    
class_list = [class_1, class_2, class_3, class_4, class_5, class_6]


applied_class_list = []

def apply_class(class_name):
    global applied_class_list
    applied_class_list.append(class_name)
    return applied_class_list

def cancel_class(class_name):
    global applied_class_list
    applied_class_list.remove(class_name)
    return applied_class_list