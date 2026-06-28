import os
import json

sessions = [1, 2, 3, 4, 5, 6, 8, 9]

for s in sessions:
    # Quiz placeholder
    quiz_path = f"d:/PARA/Projects/second-brain/05-Projects/lms-hub/courses/cslt2026/content/questions/session-{s}.json"
    quiz_data = {
        "session": s,
        "chapter": "",
        "title": f"Buổi {s} (Chưa cập nhật)",
        "time_limit_minutes": 10,
        "questions": []
    }
    with open(quiz_path, 'w', encoding='utf-8') as f:
        json.dump(quiz_data, f, ensure_ascii=False, indent=2)

    # Lesson placeholder
    lesson_path = f"d:/PARA/Projects/second-brain/05-Projects/lms-hub/courses/cslt2026/content/lessons/Buoi_0{s}.html"
    lesson_html = f"<div class=\"container\"><div class=\"content-card\"><h1>Buổi {s} (Chưa cập nhật)</h1></div></div>"
    with open(lesson_path, 'w', encoding='utf-8') as f:
        f.write(lesson_html)

print("Placeholders created successfully.")
