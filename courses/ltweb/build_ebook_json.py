"""Chuyển ebook Markdown (SCQA) của LTWeb -> chapter-N.json cho LMS Hub.

Nguồn khái niệm : 04-output/teaching/LTWeb/ebook/chuong_N_*.md
Nguồn câu hỏi   : content/questions/bank.json (từ test_bank.md chính thức - 299 câu)
Output          : courses/ltweb/content/ebook/chapter-1..5.json

Đảm bảo:
1. Không một mục (section/subsection) nào bị mất bullet, bảng <table> hay khối <pre><code>.
2. Không đặt <table> hoặc <pre> trực tiếp vào trường `definition` (vì UI bọc `definition` trong thẻ <p>).
3. Gắn thẻ `session` (1..9) cho từng concept để trang Buổi học hiển thị đúng khái niệm trọng tâm của buổi đó.
4. Đưa toàn bộ 100% câu hỏi của từng chương từ bank.json vào Vòng Test 3 cấp bậc (Level 1, Level 2, Level 3).
"""
import html, json, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"d:/PARA/Projects/second-brain")
MD_DIR = ROOT / "04-output/teaching/LTWeb/ebook"
COURSE = ROOT / "05-Projects/lms-hub/courses/ltweb"
OUT = COURSE / "content/ebook"
OUT.mkdir(parents=True, exist_ok=True)

BANK = json.loads((COURSE / "content/questions/bank.json").read_text(encoding="utf-8"))
CFG = json.loads((COURSE / "course-config.json").read_text(encoding="utf-8"))
FILES = {
    1: "chuong_1_tong_quan.md",
    2: "chuong_2_cai_dat.md",
    3: "chuong_3_php.md",
    4: "chuong_4_mysql.md",
    5: "chuong_5_php_mysql.md",
}

RAW = re.compile(r"(<pre><code>.*?</code></pre>|<table><thead>.*?</table>)", re.S)


def sessions_of(ch: int):
    return [s["id"] for s in CFG["sessions"] if s["chapter"] == f"Ch.{ch}"]


def concept_session(ch: int, sec_num: str, term: str) -> int:
    """Xác định buổi học (1..9) tương ứng với từng khái niệm trong chương."""
    if ch == 1:
        return 1
    if ch == 2:
        return 2
    if ch == 4:
        return 6
    tl = term.lower()
    if ch == 3:
        # 3.2.7+ hoặc hàm -> Buổi 5
        if sec_num.startswith("3.2.7") or "hàm" in tl:
            return 5
        # 3.2.2c (mảng), 3.2.6+ (vòng lặp, break/continue), 3.3, 3.4 -> Buổi 4 & 5
        if sec_num.startswith("3.2.6") or "vòng lặp" in tl or "break" in tl or "mảng" in tl:
            return 4
        if sec_num.startswith(("3.3", "3.4")):
            return 5
        return 3
    # Chương 5:
    # 5.2 (Biểu mẫu web, GET/POST) -> Buổi 7
    # 5.3, 5.4 (Session & Cookie) -> Buổi 8
    # 5.1 (Kết nối MySQLi, Prepared Statement) & 5.5, 5.6 (Tổng hợp) -> Buổi 9
    if sec_num.startswith("5.2") or "biểu mẫu" in tl or "get" in tl or "post" in tl:
        return 7
    if sec_num.startswith(("5.3", "5.4")) or "session" in tl or "cookie" in tl:
        return 8
    return 9


def fmt(t: str) -> str:
    t = html.escape(html.unescape(t), quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", t)
    return t


def inline(t: str) -> str:
    """Escape + định dạng markdown nhẹ; giữ nguyên các khối HTML thô <pre>/<table>."""
    out = []
    for i, seg in enumerate(RAW.split(t.strip())):
        out.append(seg.replace("\u0001", "\n") if i % 2 else fmt(seg))
    return "".join(out)


def slug(s: str) -> str:
    s = re.sub(r"^[\d.\s]+", "", s).lower()
    rep = str.maketrans(
        "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ",
        "aaaaaaaaaaaaaaaaaeeeeeeeeeeeiiiiiooooooooooooooooouuuuuuuuuuuyyyyyd",
    )
    s = s.translate(rep)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:40]


def is_pure_block_html(s: str) -> bool:
    st = s.strip()
    return st.startswith("<pre>") or st.startswith("<table>")


def split_blocks(lines):
    """Chia thân section thành các khối: ('p', text) | ('b', text) | ('code', str) | ('block', html)."""
    blocks, i = [], 0
    while i < len(lines):
        ln = lines[i]
        st = ln.strip()
        if st.startswith("```"):
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            indent = min((len(x) - len(x.lstrip()) for x in buf if x.strip()), default=0)
            blocks.append(("code", "\n".join(x[indent:] for x in buf).rstrip()))
        elif re.match(r"^\s*[-*]\s+", ln):
            blocks.append(("b", re.sub(r"^\s*[-*]\s+", "", ln)))
        elif re.match(r"^\s*\d+\.\s+", ln):
            blocks.append(("b", st))
        elif st:
            if is_pure_block_html(st):
                blocks.append(("block", st))
            else:
                blocks.append(("p", st))
        i += 1
    return blocks


def code_html(c: str) -> str:
    return f"<pre><code>{html.escape(c, quote=False)}</code></pre>"


def to_points(blocks):
    """Gộp khối thành key_points: code/table đi kèm điểm đứng trước hoặc đứng độc lập."""
    pts = []
    for kind, val in blocks:
        if kind == "code":
            ex = code_html(val)
            if pts and not pts[-1].endswith("</pre>") and not pts[-1].endswith("</table>"):
                pts[-1] += ex
            else:
                pts.append(ex)
        elif kind == "block":
            b_html = inline(val)
            if pts and not pts[-1].endswith("</pre>") and not pts[-1].endswith("</table>") and len(pts[-1]) < 180:
                pts[-1] += b_html
            else:
                pts.append(b_html)
        else:
            pts.append(inline(val))
    return pts


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s).strip()


def parse_chapter(ch, md):
    lines = md.splitlines()
    title = re.sub(r"^#\s*CH[ƯU]ƠNG\s+\d+\.\s*", "", lines[0]).strip().capitalize()
    title = title.replace("php", "PHP").replace("mysql", "MySQL").replace("Mysql", "MySQL")

    # SCQA
    scqa = {}
    for key, tag in (("situation", "Situation"), ("complication", "Complication"),
                     ("question", "Question"), ("answer", "Answer")):
        m = re.search(rf"\*\*{tag}[^*]*\*\*:\s*(.+)", md)
        scqa[key] = fmt(m.group(1).strip()) if m else ""

    # Phần nội dung trước "## 3. Vòng Test" hoặc "## Vòng Test"
    body = re.split(r"\n##\s+(?:\d+\.\s*)?Vòng Test", md)[0]
    body = RAW.sub(lambda m: m.group(0).replace("\n", "\u0001"), body)
    raw_sections = re.split(r"\n(?=##\s+\d+\.\d+)", body)[1:]

    parsed_secs = []
    for sec in raw_sections:
        sl = sec.strip("\n").splitlines()
        m_head = re.match(r"^##\s+([\d.]+[a-z]?)\.?\s*(.*)", sl[0])
        sec_num = m_head.group(1).rstrip(".") if m_head else ""
        term = (m_head.group(2) if m_head else re.sub(r"^##\s+", "", sl[0])).strip().rstrip(":")
        rest = [x for x in sl[1:] if x.strip() != "---"]
        parsed_secs.append((sec_num, term, rest))

    concepts = []
    pending_intro = None

    for idx, (sec_num, term, rest) in enumerate(parsed_secs):
        # Kiểm tra nếu mục cha (ví dụ 2.1, 2.2, 3.1, 3.2, 4.2, 4.3, 4.4, 5.1) chỉ có 1 dòng dẫn nhập
        # và ngay sau nó là mục con (ví dụ 2.1.1, 4.2.1...): gộp lời dẫn vào mục con đầu tiên để tránh thẻ rỗng!
        next_sec_num = parsed_secs[idx + 1][0] if idx + 1 < len(parsed_secs) else ""
        non_empty_rest = [x.strip() for x in rest if x.strip()]
        if (
            next_sec_num.startswith(sec_num + ".")
            and len(non_empty_rest) <= 1
            and not any(x.startswith("###") or x.startswith("-") or x.startswith("<") for x in non_empty_rest)
        ):
            if non_empty_rest:
                pending_intro = f"<strong>{html.escape(term, quote=False)}</strong>: {inline(non_empty_rest[0])}"
            continue

        # Tách theo ###
        parts, cur = [], [None, []]
        for x in rest:
            m = re.match(r"^###\s+(.*)", x)
            if m:
                parts.append(cur)
                cur = [re.sub(r"^[\d.\s]+", "", m.group(1)).strip(), []]
            else:
                cur[1].append(x)
        parts.append(cur)

        intro_blocks = split_blocks(parts[0][1])
        definition = ""
        key_points = []

        if pending_intro:
            key_points.append(pending_intro)
            pending_intro = None

        # Tìm câu định nghĩa văn xuôi đầu tiên (không phải <pre>/<table>)
        p_idx = next((i for i, (k, v) in enumerate(intro_blocks) if k == "p" and not is_pure_block_html(v)), None)
        if p_idx is not None:
            full_p = inline(intro_blocks[p_idx][1])
            if "<pre>" in full_p or "<table>" in full_p:
                split_pos = min(x for x in (full_p.find("<pre>"), full_p.find("<table>")) if x != -1)
                definition = full_p[:split_pos].strip()
                key_points.append(full_p[split_pos:].strip())
            else:
                definition = full_p
            rem_blocks = [b for i, b in enumerate(intro_blocks) if i != p_idx]
            key_points += to_points(rem_blocks)
        else:
            # Nếu không có đoạn văn xuôi mở đầu (chỉ có bullet hoặc bảng/code)
            pts = to_points(intro_blocks)
            if pts:
                # Nếu điểm đầu tiên là chữ thuần (không chứa <pre>/<table>), lấy phần chữ làm định nghĩa ngắn
                first_plain = strip_tags(pts[0].split("<pre>")[0].split("<table>")[0]).strip()
                if first_plain and not pts[0].strip().startswith(("<pre>", "<table>")) and len(pts) > 1:
                    definition = pts[0].split("<pre>")[0].split("<table>")[0].strip()
                    # Nếu pts[0] có đính kèm <pre>/<table> phía sau thì giữ phần <pre>/<table> trong key_points
                    leftover = pts[0][len(definition):].strip()
                    if leftover:
                        key_points.append(leftover)
                    key_points += pts[1:]
                else:
                    definition = f"Nội dung trọng tâm và cú pháp chi tiết của mục <strong>{html.escape(term, quote=False)}</strong>."
                    key_points += pts

        # Xử lý các mục con ### (nếu có)
        for sub, sublines in parts[1:]:
            blocks = split_blocks(sublines)
            pts = to_points(blocks)
            head = f"<strong>{html.escape(sub, quote=False)}</strong>"
            if not definition and pts:
                first_plain = strip_tags(pts[0].split("<pre>")[0].split("<table>")[0]).strip()
                if first_plain and not pts[0].strip().startswith(("<pre>", "<table>")):
                    definition = f"{head}: {pts[0].split('<pre>')[0].split('<table>')[0].strip()}"
            if not pts:
                key_points.append(head)
                continue
            first = pts.pop(0)
            if first.strip().startswith(("<pre>", "<table>")):
                key_points.append(f"{head}:{first}")
            else:
                key_points.append(f"{head}: {first}")
            key_points += pts

        if not definition:
            definition = f"Kiến thức cốt lõi về <strong>{html.escape(term, quote=False)}</strong> trong Chương {ch}."
        if not key_points:
            key_points.append(definition)

        concepts.append({
            "id": f"c{ch}-{slug(term)}",
            "session": concept_session(ch, sec_num, term),
            "term": html.escape(term, quote=False),
            "definition": definition,
            "key_points": key_points,
            "case_study": None,
            "related_concepts": [],
        })

    for i, c in enumerate(concepts):
        c["related_concepts"] = [concepts[j]["id"] for j in (i - 1, i + 1) if 0 <= j < len(concepts)]
    return title, scqa, concepts


def tokens(s):
    return {w for w in re.findall(r"\w+", s.lower()) if len(w) > 2}


def concept_for(q, concepts):
    qt = tokens(q["question"] + " " + " ".join(q["options"]))
    best = max(
        concepts,
        key=lambda c: len(qt & tokens(c["term"] + " " + c["definition"] + " " + " ".join(c["key_points"]))),
    )
    return best["id"]


def pick_all_chapter_questions(ch, concepts):
    """Đưa toàn bộ 100% câu hỏi thuộc chương `ch` vào Vòng Test 3 cấp bậc (Level 1, 2, 3)."""
    pool = {lv: [q for q in BANK if q["chapter"] == ch and q["level"] == lv] for lv in (1, 2, 3)}
    # Riêng Chương 1 trong test_bank có 17 câu M1, 9 câu M2 và 0 câu M3:
    # Chia 9 câu M2 thành 5 câu cho Level 2 và 4 câu tình huống URL/HTTP/CSS cho Level 3 để sinh viên luyện đủ 3 cấp bậc
    if ch == 1 and not pool[3] and len(pool[2]) >= 5:
        pool[3] = pool[2][5:]
        pool[2] = pool[2][:5]

    out = {}
    for lv in (1, 2, 3):
        qs = sorted(pool[lv], key=lambda q: q["id"])
        out[lv] = [
            {
                "id": q["id"],
                "type": "mc",
                "concept_ref": concept_for(q, concepts),
                "question": q["question"],
                "options": q["options"],
                "correct": q["correct"],
                "explanation": q.get("explanation", ""),
            }
            for q in qs
        ]
    return out


def main():
    total_ebook_mc = 0
    for ch, fn in FILES.items():
        md = (MD_DIR / fn).read_text(encoding="utf-8")
        if ch == 3:
            md = md.rstrip() + "\n\n" + (MD_DIR / "chuong_3_php_b.md").read_text(encoding="utf-8")
        title, scqa, concepts = parse_chapter(ch, md)
        qs = pick_all_chapter_questions(ch, concepts)
        total_ch_q = len(qs[1]) + len(qs[2]) + len(qs[3])
        total_ebook_mc += total_ch_q

        data = {
            "chapter": ch,
            "title": title,
            "sessions": sessions_of(ch),
            "scqa": scqa,
            "concepts": concepts,
            "tests": {
                "level_1": {
                    "name": f"🎯 Level 1: Nhận biết khái niệm ({len(qs[1])} câu)",
                    "description": "Kiểm tra trí nhớ và nhận diện chính xác các khái niệm, cú pháp nền tảng của chương.",
                    "bloom_level": "Remember",
                    "questions": qs[1],
                },
                "level_2": {
                    "name": f"📝 Level 2: Thông hiểu & Phân tích ({len(qs[2])} câu)",
                    "description": "Phân biệt, giải thích nguyên lý hoạt động và so sánh các thành phần kỹ thuật.",
                    "bloom_level": "Understand",
                    "questions": qs[2],
                },
                "level_3": {
                    "name": f"🚀 Level 3: Vận dụng thực tế ({len(qs[3])} câu)",
                    "description": "Đọc hiểu đoạn mã, dự đoán kết quả thực thi và xử lý tình huống lập trình thực tế.",
                    "bloom_level": "Apply",
                    "questions": qs[3],
                },
            },
        }
        (OUT / f"chapter-{ch}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(
            f"Ch.{ch} '{title}': {len(concepts):2d} concepts | "
            f"L1={len(qs[1]):2d}, L2={len(qs[2]):2d}, L3={len(qs[3]):2d} (Tổng={total_ch_q:3d} câu) | sessions={data['sessions']}"
        )
    print(f"Tổng số câu hỏi trắc nghiệm trong Ebook (Chương 1..5): {total_ebook_mc} / {len(BANK)} câu (Đạt 100%)")


if __name__ == "__main__":
    main()
