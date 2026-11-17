# Tự sửa bài giảng chuyển động

Có hai mức. Mức 1 không cần cài gì và đủ cho phần lớn việc sửa.

## Mức 1 — Sửa ngay trong file HTML (phím E)

1. Mở file `.html` bằng **Chrome** hoặc **Edge**. Đi tới slide cần sửa.
2. Nhấn **E**. Slide hiện ở trạng thái đầy đủ (mọi vật thể đã ra hết), góc trái có thanh hướng dẫn.
3. Sửa:

| Muốn làm | Thao tác |
|---|---|
| Di chuyển vật thể (thẻ, card, giấy nhớ, con dấu, tiêu đề, băng keo) | Kéo thả |
| Di chuyển vòng khoanh, mũi tên, nét gạch đỏ | Kéo ngay trên nét (ở chế độ sửa nét được làm dày để dễ bắt) |
| Dịch từng chút | Bấm chọn rồi ←↑→↓ (1px), giữ Shift (10px) |
| Hẹp / rộng hơn | `[` và `]` (giữ Shift: bước 50px) |
| Sửa chữ | Nhấp đúp vào chữ → gõ → **Enter** xong, **Esc** huỷ, Shift+Enter xuống dòng |
| Bỏ một vật thể | Chọn → **Delete** |
| Hoàn tác | **Ctrl+Z** |
| Sang slide khác khi đang sửa | **PageUp / PageDown** |
| Lưu | **Ctrl+S** → chọn ghi đè file cũ (hoặc lưu tên mới) |
| Thoát, xem lại chuyển động | **E** |

Mẹo:
- Kéo một vật thể thì mũi tên và vòng khoanh nối với nó tự vẽ lại theo vị trí mới.
- Chữ vẽ trong hình (nhãn trên xe, số trên đồng hồ, chữ trong đèn) không sửa ở đây được — dùng mức 2.
- Nếu lỡ tay, chưa lưu thì đóng tab mà không lưu (trình duyệt sẽ hỏi lại).

## Mức 2 — Sửa lời giảng, beat, hiệu ứng (VS Code)

Cài một lần: **VS Code** (code.visualstudio.com) và **Python** (python.org, khi cài nhớ tick "Add to PATH").

Mở file `deck.js`. Mỗi slide trông như sau:

```js
{
  chapter: "demo", tape: "09 · Demo 1 · Prompt",          // băng keo đầu trang
  html: (C) => `
    ${C.title("Prompt", "tóm tắt bài báo", { id: "t", y: 120, size: "sm", inline: true })}
    ${C.card({ id: "k1", x: 150, y: 285, w: 500, kick: "1 · …", title: "…", body: "…" })}`,
  beats: [
    { say: "Câu bạn nói ở beat này.", note: "ghi chú riêng",
      run: (tl, fx) => tl.add(fx.title("#t")) },
    { say: "Câu tiếp theo.", run: (tl, fx) => tl.add(fx.drop("#k1")) },
  ],
},
```

| Muốn làm | Sửa ở đâu |
|---|---|
| Đổi lời giảng (hiện ở cửa sổ P, phụ đề, nhịp tự chạy) | chuỗi trong `say: "…"` |
| Đổi tiêu đề | `C.title("phần xanh", "phần đỏ", …)` |
| Đổi vị trí / độ rộng | `x:` `y:` `w:` (khung 1920 × 1080, timeline đáy bắt đầu từ y ≈ 940) |
| Đổi kiểu xuất hiện | thay `fx.drop` bằng `fx.place`, `fx.slide("#k1", { from: "left" })`, `fx.pop`, `fx.in`… |
| Thêm một beat | chép một dòng `{ say: …, run: … },` rồi sửa |
| Cho 2 thứ xuất hiện cùng lúc | `tl.add(fx.drop("#a")).add(fx.drop("#b"), 0)` — số `0` = cùng thời điểm đầu beat |
| Cho thứ 2 ra sau 0,5 giây | `.add(fx.drop("#b"), 0.5)` |
| Khoanh / gạch / mũi tên | `fx.circle("#k1")`, `fx.strike("#k1 .face")`, `fx.arrow("#a", "#b")` |
| Dừng lâu hơn khi tự chạy | thêm `hold: 4` (giây) vào beat |

Build lại (mở Terminal trong VS Code, đứng ở thư mục skill):

```
python scripts/build.py duong-dan/deck.js -o bai-moi.html --edits bai-da-sua-bang-phim-E.html
```

`--edits` giữ lại những gì bạn đã kéo thả, sửa chữ ở mức 1. Không có thì bỏ phần đó.

Lỗi hay gặp khi sửa `deck.js`: thiếu dấu phẩy giữa hai beat, thiếu dấu `` ` `` đóng ở cuối `html`, hoặc dùng dấu `"` bên trong chuỗi `"…"` (dùng `“ ”` thay thế). Nếu mở file thấy trắng trang, nhấn F12 → tab Console để xem dòng lỗi.

## Khi nào nhờ Claude

Thêm slide mới, đổi ẩn dụ hình ảnh, viết lại cả phần, hay thêm loại vật thể mới. Gom tất cả yêu cầu vào **một tin nhắn** kèm file HTML đã sửa — Claude sẽ giữ các chỉnh sửa của bạn.
