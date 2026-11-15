"""Chuyển test_bank.md (LTWeb) -> ngân hàng câu hỏi JSON + quiz từng buổi + đề thi giữa kỳ/tổng hợp cho LMS Hub.

Output (trong content/questions/ và content/exams/):
  bank.json        : toàn bộ 299 câu hỏi (id, chapter, level, session, options, correct, explanation)
  session-N.json   : toàn bộ câu hỏi thuộc buổi N (đảm bảo phủ 100% 299 câu hỏi của ngân hàng đề thi)
  exams/midterm.json : 3 đề thi thử/giữa kỳ (40 câu/đề, 60 phút) bám sát 100% ma trận đề thi cuối kỳ trong Đề cương
"""
import json, re, random, sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"d:/PARA/Projects/second-brain")
SRC = ROOT / "04-output/teaching/LTWeb/test_bank.md"
COURSE_DIR = ROOT / "05-Projects/lms-hub/courses/ltweb"
OUT = COURSE_DIR / "content/questions"
EXAM_OUT = COURSE_DIR / "content/exams"
CFG = json.loads((COURSE_DIR / "course-config.json").read_text(encoding="utf-8"))
OUT.mkdir(parents=True, exist_ok=True)
EXAM_OUT.mkdir(parents=True, exist_ok=True)

LETTER = "ABCD"

# Phân loại chính xác buổi học cho Chương 3 (Buổi 3, 4, 5) và Chương 5 (Buổi 7, 8, 9)
S5_USER_FUNC = re.compile(
    r"\bfunction\b|writeMsg|familyName|swap\(|add_five|calculate\(|process\(|findValue|calc\(|myFunction|"
    r"tham số|tham biến|reference|include|require|header\.php",
    re.I,
)
S5_BUILTIN_FUNC = re.compile(
    r"var_dump|print_r|\bdate\s*\(|\bexplode\s*\(|\bimplode\s*\(|\bsort\s*\(|\basort\s*\(|\bksort\s*\(|"
    r"\brsort\s*\(|\barsort\s*\(|\bkrsort\s*\(|\bcount\s*\(|\bis_array\s*\(|\barray_key_exists\s*\(|"
    r"\bin_array\s*\(|\bisset\s*\(|\bunset\s*\(",
    re.I,
)
S4_LOOP_ARRAY = re.compile(
    r"vòng lặp|\bfor\s*\(|\bwhile\s*\(|\bdo\s*\{|do\.\.\.while|do…while|\bforeach\b|\bbreak\b|\bcontinue\b|"
    r"mảng|\barray\s*\(|\$cars|\$fruits|\$students|\$student\s*=\s*\[|\$products|\$arrCourses|"
    r"\$numbers\s*=\s*\[|\$data\s*=\s*\[|\$arr\s*=\s*\[|\$subjects\s*=\s*\[|\$credits|\$age\s*=",
    re.I,
)


def session_of(stt: int, chapter: int, q: str, correct_opt: str, all_text: str) -> int:
    if chapter == 1:
        return 1
    if chapter == 2:
        return 2
    if chapter == 4:
        return 6
    if chapter == 3:
        # Câu hỏi về thẻ rút gọn <?= $_GET['name']; ?> thuộc phần cú pháp nhúng PHP (Buổi 3)
        if stt == 59:
            return 3
        # Câu hỏi về hàm tự định nghĩa, include/require hoặc hàm dựng sẵn trong PHP -> Buổi 5
        if S5_USER_FUNC.search(all_text) or S5_BUILTIN_FUNC.search(q + " " + correct_opt):
            return 5
        # Câu hỏi về vòng lặp và mảng -> Buổi 4
        if S4_LOOP_ARRAY.search(q + " " + correct_opt):
            return 4
        # Còn lại: cú pháp PHP, biến, hằng, kiểu dữ liệu, toán tử, biểu thức, điều kiện if/else -> Buổi 3
        return 3

    # Chương 5 (Buổi 7: Form & GET/POST/QueryString, Buổi 8: Session & Cookie, Buổi 9: Kết nối PHP-MySQL & Tổng hợp)
    if 291 <= stt <= 300:
        return 9
    if stt in (191, 192, 194, 210, 213, 219) or (281 <= stt <= 290):
        return 8
    if stt in (171, 195, 198, 200, 201, 209, 212, 214):
        return 9
    return 7


def build_explanation(stt: int, ch: int, lvl: int, q: str, correct_letter: str, correct_text: str) -> str:
    """Sinh lời giải thích rõ ràng, bám sát giáo trình cho từng câu hỏi."""
    ql = q.lower()
    cl = correct_text.lower()

    # Giải thích chuyên biệt theo chủ đề
    if ch == 1:
        if "404" in ql:
            return f"Đáp án đúng là {correct_letter}: Mã trạng thái HTTP 404 (Not Found) báo hiệu web server không tìm thấy tài nguyên theo URL mà trình duyệt yêu cầu."
        if "200" in ql:
            return f"Đáp án đúng là {correct_letter}: Mã trạng thái HTTP 200 (OK) cho biết web server đã tiếp nhận và xử lý yêu cầu HTTP thành công."
        if "url" in ql or "port" in ql or "8080" in ql or "querystring" in ql or "tham số" in ql:
            return f"Đáp án đúng là {correct_letter}: Theo cấu trúc URL scheme://host[:port]/path?querystring, phần sau dấu ':' là cổng (port, mặc định HTTP là 80), sau '/' là đường dẫn (path) và sau '?' là chuỗi truy vấn (query string) truyền tham số."
        if "css" in ql or "style" in ql or "font" in ql or "background" in ql or "margin" in ql or "padding" in ql or "border" in ql:
            return f"Đáp án đúng là {correct_letter}: Trong CSS, bộ chọn thẻ viết tên thẻ, bộ chọn class dùng dấu chấm (.class), bộ chọn id dùng dấu thăng (#id); có 3 cách nhúng CSS là Inline (thuộc tính style), Internal (thẻ <style>) và External (thẻ <link>)."
        if "html" in ql or "thẻ" in ql or "<a" in ql or "<img" in ql or "<ul" in ql or "<ol" in ql or "<table" in ql:
            return f"Đáp án đúng là {correct_letter}: Theo chuẩn HTML5, mỗi thẻ đảm nhận một vai trò cấu trúc riêng (<h1>-<h6> tiêu đề, <p> đoạn văn, <a href='...'> liên kết, <img src='...'> hình ảnh, <ul>/<ol>/<li> danh sách, <table>/<tr>/<td> bảng)."
        return f"Đáp án đúng là {correct_letter} ({correct_text}): Trong mô hình Client - Server, trình duyệt (Web Client) gửi HTTP Request đến Web Server; Web tĩnh trả trực tiếp HTML/CSS, còn Web động thực thi mã phía server và kết nối CSDL trước khi trả kết quả HTML."

    if ch == 2:
        if "httpd.conf" in cl or "httpd.conf" in ql:
            return f"Đáp án đúng là {correct_letter}: Tập tin cấu hình chính của Apache HTTP Server là httpd.conf (dùng để đổi cổng Listen 80/8080, ServerName, DocumentRoot)."
        if "php.ini" in cl or "php.ini" in ql:
            return f"Đáp án đúng là {correct_letter}: Tập tin cấu hình của PHP là php.ini (dùng để bật/tắt hiển thị lỗi display_errors, cấu hình dung lượng tải file upload_max_filesize, post_max_size, múi giờ)."
        if "htdocs" in cl or "www" in cl or "thư mục" in ql:
            return f"Đáp án đúng là {correct_letter}: Với XAMPP, mã nguồn đặt trong thư mục htdocs (còn với WAMP là thư mục www). Tập tin mặc định được tự động chạy khi truy cập thư mục là index.php hoặc index.html."
        return f"Đáp án đúng là {correct_letter} ({correct_text}): Bộ công cụ XAMPP/WAMP/MAMP đóng gói sẵn Apache Web Server, PHP và MySQL/MariaDB kèm phpMyAdmin giúp tạo môi trường máy chủ cục bộ (localhost) để phát triển và kiểm thử ứng dụng web."

    if ch == 3:
        if "nháy đơn" in ql or "nháy kép" in ql or "'i love" in ql or '"i love' in ql:
            return f"Đáp án đúng là {correct_letter}: Trong PHP, chuỗi đặt trong dấu nháy kép (\" \") sẽ nội suy (thay thế) tên biến bằng giá trị của biến, còn chuỗi đặt trong dấu nháy đơn (' ') sẽ in nguyên văn tên biến."
        if "++" in q or "--" in q:
            return f"Đáp án đúng là {correct_letter} ({correct_text}): Toán tử tiền tố (++$x, --$x) tăng/giảm giá trị biến trước rồi mới trả về giá trị trong biểu thức; còn toán tử hậu tố ($x++, $x--) trả về giá trị hiện tại cho biểu thức trước rồi mới tăng/giảm biến."
        if "===" in q or "!==" in q or "==" in q:
            return f"Đáp án đúng là {correct_letter}: Trong PHP, toán tử '==' chỉ so sánh giá trị (có tự động ép kiểu), còn '===' so sánh nghiêm ngặt cả giá trị lẫn kiểu dữ liệu (tương tự '!=' so sánh giá trị và '!==' so sánh cả giá trị lẫn kiểu)."
        if "asort" in cl or "ksort" in cl or "sort(" in cl or "sắp xếp" in ql:
            return f"Đáp án đúng là {correct_letter}: Trong PHP, sort() sắp xếp mảng chỉ số tăng dần (mất khóa chuỗi); asort() sắp xếp mảng kết hợp tăng dần theo giá trị (value) và giữ khóa; ksort() sắp xếp mảng kết hợp tăng dần theo khóa (key)."
        if "explode" in cl or "implode" in cl or "explode" in ql or "implode" in ql:
            return f"Đáp án đúng là {correct_letter}: Hàm explode(separator, string) tách chuỗi thành mảng dựa vào ký tự phân cách; ngược lại hàm implode(separator, array) nối các phần tử mảng thành một chuỗi."
        if "foreach" in ql or "while" in ql or "for (" in ql or "for(" in ql or "vòng lặp" in ql:
            return f"Đáp án đúng là {correct_letter} ({correct_text}): Vòng lặp for/while kiểm tra điều kiện trước mỗi lần lặp; do...while thực thi ít nhất 1 lần trước khi kiểm tra điều kiện; foreach duyệt qua từng phần tử của mảng. Lệnh break thoát hẳn vòng lặp, còn continue bỏ qua phần còn lại của lần lặp hiện tại để sang lần lặp kế tiếp."
        if "function" in ql or "tham chiếu" in ql or "tham biến" in ql or "hàm" in ql:
            return f"Đáp án đúng là {correct_letter} ({correct_text}): Hàm trong PHP khai báo bằng từ khóa function. Mặc định tham số truyền theo giá trị (không làm đổi biến gốc bên ngoài); nếu thêm dấu '&' trước tham số (truyền tham chiếu) thì mọi thay đổi bên trong hàm sẽ tác động trực tiếp lên biến gốc."
        return f"Đáp án đúng là {correct_letter} ({correct_text}): Theo quy tắc cú pháp PHP (Chương 3), mã PHP đặt trong <?php ... ?>, câu lệnh kết thúc bằng ';', biến bắt đầu bằng '$' + chữ cái hoặc '_' và phân biệt chữ hoa/thường."

    if ch == 4:
        if "join" in ql or "join" in cl:
            return f"Đáp án đúng là {correct_letter}: INNER JOIN chỉ lấy các dòng khớp ở cả 2 bảng; LEFT JOIN lấy toàn bộ bảng bên trái (phần không khớp ở bảng phải nhận NULL); RIGHT JOIN lấy toàn bộ bảng bên phải (phần không khớp ở bảng trái nhận NULL)."
        if "group by" in ql or "having" in ql or "count(" in ql or "avg(" in ql:
            return f"Đáp án đúng là {correct_letter}: Mệnh đề GROUP BY gom nhóm các bản ghi theo giá trị cột để tính hàm tổng hợp (COUNT, SUM, AVG, MAX, MIN). WHERE lọc dòng trước khi gom nhóm, còn HAVING lọc nhóm sau khi đã GROUP BY."
        if "update" in cl or "delete" in cl or "insert" in cl or "drop" in cl or "alter" in cl:
            return f"Đáp án đúng là {correct_letter}: Trong SQL, nhóm DDL (CREATE, ALTER, DROP) thao tác trên cấu trúc bảng/CSDL; nhóm DML (SELECT, INSERT INTO, UPDATE ... SET, DELETE FROM) thao tác trên các dòng dữ liệu. Luôn dùng WHERE khi UPDATE/DELETE để tránh sửa/xóa nhầm toàn bộ bảng."
        return f"Đáp án đúng là {correct_letter} ({correct_text}): Theo chuẩn truy vấn MySQL và quản trị phpMyAdmin (Chương 4), thứ tự mệnh đề chuẩn là SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY [ASC|DESC] -> LIMIT."

    # Chương 5
    if "prepared" in ql or "bind_param" in ql or "sql injection" in ql:
        return f"Đáp án đúng là {correct_letter}: Prepared Statement tách biệt câu lệnh SQL (với dấu chấm hỏi '?' làm vị trí giữ chỗ) và dữ liệu đầu vào qua bước prepare() -> bind_param() -> execute(), giúp chống tấn công SQL Injection và tối ưu hiệu năng khi lặp lại truy vấn."
    if "session" in ql or "cookie" in ql or "setcookie" in ql:
        return f"Đáp án đúng là {correct_letter}: Session lưu dữ liệu trạng thái trên Web Server (bảo mật hơn, cần gọi session_start() trước khi dùng $_SESSION, tự hủy khi đóng trình duyệt hoặc hết phiên), còn Cookie lưu trên trình duyệt người dùng bằng hàm setcookie() với thời gian hết hạn xác định."
    if "checkbox" in ql or "radio" in ql or "select" in ql or "textarea" in ql:
        return f"Đáp án đúng là {correct_letter}: Trong HTML Form, thuộc tính 'name' của ô nhập liệu sẽ trở thành khóa (key) trong mảng $_GET/$_POST. Các radio cùng nhóm phải có cùng 'name'; nhóm checkbox chọn nhiều giá trị cần đặt name dạng mảng (ví dụ name='vehicle[]')."
    return f"Đáp án đúng là {correct_letter} ({correct_text}): Trong xử lý Form với PHP (Chương 5), thuộc tính action chỉ định file xử lý trên server (bỏ trống sẽ gửi về chính trang hiện tại), method xác định phương thức gửi (mặc định là GET truyền qua URL query string; POST truyền trong phần thân HTTP Request bảo mật hơn)."


def parse():
    rows = SRC.read_text(encoding="utf-8").splitlines()[2:]
    bank = []
    for line in rows:
        p = [x.strip() for x in line.strip().strip("|").split(" | ")]
        if len(p) != 9:
            continue
        stt, q, o1, o2, o3, o4, ans, lvl, ch = p
        stt_i, ch_i, lvl_i = int(stt), int(ch), int(lvl)
        opts = [o1, o2, o3, o4]
        correct_idx = int(ans) - 1
        correct_letter = LETTER[correct_idx]
        correct_text = opts[correct_idx]
        all_text = " ".join([q, o1, o2, o3, o4])
        sess = session_of(stt_i, ch_i, q, correct_text, all_text)
        bank.append({
            "id": f"ltweb-q{stt_i:03d}",
            "chapter": ch_i,
            "level": lvl_i,  # 1 nhớ / 2 hiểu / 3 vận dụng (M1-M3)
            "session": sess,
            "type": "mc",
            "question": q,
            "options": [f"{LETTER[i]}. {o}" for i, o in enumerate(opts)],
            "correct": correct_letter,
            "explanation": build_explanation(stt_i, ch_i, lvl_i, q, correct_letter, correct_text),
        })
    return bank


def build_session_quiz(bank, s):
    """Đưa toàn bộ 100% câu hỏi thuộc buổi s vào session-s.json để sinh viên không bị sót bất kỳ câu nào trong test_bank."""
    pool = [q for q in bank if q["session"] == s]
    pool.sort(key=lambda q: (q["level"], q["id"]))
    meta = next(x for x in CFG["sessions"] if x["id"] == s)
    # Thời gian làm bài tỷ lệ với số lượng câu hỏi (khoảng 45-60 giây/câu, tối thiểu 20 phút)
    time_limit = max(20, int(round(len(pool) * 0.8 / 5.0) * 5))
    return {
        "session": s,
        "chapter": meta["chapter"],
        "title": meta["title"],
        "time_limit_minutes": time_limit,
        "questions": [
            {k: q[k] for k in ("id", "type", "level", "question", "options", "correct", "explanation")}
            for q in pool
        ],
    }


def build_midterm_exam(bank):
    """Tạo 3 đề thi chuẩn 40 câu (60 phút) theo đúng Ma trận Đề cương chi tiết:
    - Chương 1: 4 M1 + 4 M2 = 8 câu
    - Chương 2: 2 M1 + 2 M2 + 2 M3 = 6 câu
    - Chương 3: 4 M1 + 4 M2 + 4 M3 = 12 câu
    - Chương 4: 2 M1 + 2 M2 + 2 M3 = 6 câu
    - Chương 5: 4 M1 + 2 M2 + 2 M3 = 8 câu
    Tổng: 16 M1 + 14 M2 + 10 M3 = 40 câu.
    """
    matrix = [
        (1, 1, 4), (1, 2, 4),
        (2, 1, 2), (2, 2, 2), (2, 3, 2),
        (3, 1, 4), (3, 2, 4), (3, 3, 4),
        (4, 1, 2), (4, 2, 2), (4, 3, 2),
        (5, 1, 4), (5, 2, 2), (5, 3, 2),
    ]
    variants = []
    for v_idx in range(1, 4):
        rng = random.Random(7080 + v_idx)
        paper_qs = []
        for ch, lv, count in matrix:
            cand = [q for q in bank if q["chapter"] == ch and q["level"] == lv]
            rng.shuffle(cand)
            picked = cand[:count]
            paper_qs.extend(picked)
        variants.append({
            "variant": v_idx,
            "questions": [
                {k: q[k] for k in ("id", "type", "chapter", "level", "question", "options", "correct", "explanation")}
                for q in paper_qs
            ],
        })
    return {
        "exam_id": "midterm",
        "title": "Đề kiểm tra tổng hợp & Thi thử cuối kỳ (Chuẩn Ma trận Đề cương 40 câu)",
        "time_limit_minutes": 60,
        "scope": "Chương 1 - Chương 5 (16 câu Mức 1 Nhận biết, 14 câu Mức 2 Thông hiểu, 10 câu Mức 3 Vận dụng)",
        "variants": variants,
    }


def main():
    bank = parse()
    (OUT / "bank.json").write_text(json.dumps(bank, ensure_ascii=False, indent=2), encoding="utf-8")
    total_in_sessions = 0
    for s in range(1, 10):
        quiz = build_session_quiz(bank, s)
        (OUT / f"session-{s}.json").write_text(json.dumps(quiz, ensure_ascii=False, indent=2), encoding="utf-8")
        c = Counter(q["level"] for q in quiz["questions"])
        total_in_sessions += len(quiz["questions"])
        print(f"Buổi {s} ({quiz['chapter']} - {quiz['title']}): {len(quiz['questions']):2d} câu (M1={c[1]}, M2={c[2]}, M3={c[3]}) | {quiz['time_limit_minutes']} phút")

    exam = build_midterm_exam(bank)
    (EXAM_OUT / "midterm.json").write_text(json.dumps(exam, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Tổng số câu trong bank.json: {len(bank)} | Tổng số câu trong session-1..9.json: {total_in_sessions} (Đạt 100%)")
    print(f"Đã tạo midterm.json với {len(exam['variants'])} đề thi x {len(exam['variants'][0]['questions'])} câu.")


if __name__ == "__main__":
    main()
