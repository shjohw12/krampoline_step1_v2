from django.shortcuts import render, HttpResponse

# Create your views here.

# class = [class_id, due_date, loc, now_participants, max_participants, how_much, teacher_name, teacher_article, class_name, class_article, class_detail, is_closed]
class_1 = {"class_id": 1, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}             #" "
class_2 = {"class_id": 1, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
class_3 = {"class_id": 1, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
class_4 = {"class_id": 1, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
class_5 = {"class_id": 1, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}
class_6 = {"class_id": 1, "due_date": '2025-07-12', "loc": "제주시 이도2동", "now_participants": 2, "max_participants": 10, "how_much": 15000, "teacher_name": "해녀 김바당", "teacher_article": "20년 경력 바다의 이야기꾼", "class_name": "해녀의 바당요리", "class_article": "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께 해요", "class_detail": "제주의 인심이 담겨 있다는 별미 성게국과 임금님께 진상되던 옥돔을 직접 구워 맛보면 제주의 바다가 펼쳐질거에요.", "is_closed": False}



class_list = [class_1, class_2, class_3, class_4, class_5, class_6]


def function0(request): #main
    global class_list
    lst = []
    for x in class_list:
        lst.append(x)
    return str(lst)
    
def function1(request): #class
    return
    
def function2(request): #category
    return