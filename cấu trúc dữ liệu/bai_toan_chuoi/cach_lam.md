# Đề bài

---

## Bài 1: Tìm chuỗi con trong đoạn văn (Không dùng hàm có sẵn)

**Yêu cầu:**

Cho một đoạn văn (String). Viết chương trình tìm một chuỗi (vài từ) trong đoạn văn đó.

**Ràng buộc:**

- **KHÔNG** dùng các hàm có sẵn của Python như: `find()`, `index()`, `in`, `count()`, `split()`, `replace()`,...
- Phải tự viết thuật toán duyệt và so sánh từng ký tự.

**Output:**

- Vị trí (index) xuất hiện của chuỗi trong đoạn văn
- Số lần xuất hiện

---

## Bài 2: Ứng dụng – Module đếm xe qua ngã tư

**Bối cảnh:**

Một camera giao thông lưu dữ liệu các xe đi qua ngã tư vào file. Mỗi dòng trong file chứa thông tin:

```text
biển_số, x, y, thời_gian
```

Trong đó:

- `biển_số`: Chuỗi ký tự (ví dụ: `"5x-1234"`, `"29A-5678"`)
- `x`, `y`: Tọa độ vị trí xe
- `thời_gian`: Thời điểm xe đi qua (định dạng `"HH:MM"` hoặc `"HH:MM:SS"`)

**Yêu cầu:**

Viết module đọc file dữ liệu và **đếm số lượng xe có biển số chứa chuỗi `"5x"`** xuất hiện tại ngã tư trong khoảng thời gian từ **17h đến 19h**.

**Ràng buộc:**

- **KHÔNG** dùng hàm có sẵn để tách chuỗi (không dùng `split()`)
- **KHÔNG** dùng hàm có sẵn để tìm chuỗi con (không dùng `find()`, `in`)
- Phải tự viết logic tách giờ và kiểm tra chuỗi

**Output:**

- Tổng số xe thỏa mãn điều kiện
- Danh sách chi tiết các xe (biển số, tọa độ, thời gian)

---

### Ví dụ dữ liệu đầu vào

File `bienso_xe.txt`:

```text
bien_so,x,y,thoi_gian
5x-1234,106.7,10.8,16:45
5x-5678,106.7,10.8,17:30
29A-1111,106.7,10.8,18:00
5x-9999,106.7,10.8,18:45
5x-0000,106.7,10.8,19:30
```

### Kết quả mong đợi

```text
Tổng số xe '5x' từ 17h-19h: 2

Chi tiết:
  Biển số: 5x-5678 | Tọa độ: (106.7, 10.8) | Thời gian: 17:30
  Biển số: 5x-9999 | Tọa độ: (106.7, 10.8) | Thời gian: 18:45
```

---

# Giải thích chi tiết cách làm

---

## Phần 1: Tìm chuỗi con trong đoạn văn

### 1.1. Ý tưởng cốt lõi

Giả sử em có:

```text
Đoạn văn:  "ABC5xDEF"
Chuỗi tìm: "5x"
```

Em sẽ dùng **2 con trỏ** (2 vòng lặp):

- **Vòng lặp ngoài (`i`):** duyệt qua từng vị trí trong đoạn văn.
- **Vòng lặp trong (`j`):** tại mỗi vị trí `i`, so sánh từng ký tự với chuỗi cần tìm.

### 1.2. Ví dụ từng bước

```text
Đoạn văn:  "ABC5xDEF"
Index:      0 1 2 3 4 5 6 7
Chuỗi tìm: "5x" (độ dài = 2)
```

**Bước 1:** `i = 0`, so sánh bắt đầu từ vị trí 0

```text
Đoạn văn:  A B C 5 x D E F
             ↑
Chuỗi tìm: 5 x
           ↑
→ 'A' != '5' → KHÔNG KHỚP, sang i tiếp theo
```

**Bước 2:** `i = 1`, so sánh bắt đầu từ vị trí 1

```text
Đoạn văn:  A B C 5 x D E F
               ↑
Chuỗi tìm: 5 x
           ↑
→ 'B' != '5' → KHÔNG KHỚP
```

**Bước 3:** `i = 2`

```text
→ 'C' != '5' → KHÔNG KHỚP
```

**Bước 4:** `i = 3`, so sánh bắt đầu từ vị trí 3

```text
Đoạn văn:  A B C 5 x D E F
                   ↑ ↑
Chuỗi tìm: 5 x
           ↑ ↑
→ '5' == '5' ✓
→ 'x' == 'x' ✓
→ KHỚP TOÀN BỘ → Tìm thấy tại vị trí i = 3
```

### 1.3. Tại sao vòng lặp ngoài chỉ chạy đến `n - m + 1`?

```text
Đoạn văn:  "ABC5xDEF" (n = 8)
Chuỗi tìm: "5x"       (m = 2)

Vị trí cuối cùng có thể bắt đầu khớp: 8 - 2 = 6
Nếu i = 7: chỉ còn 1 ký tự 'F', không đủ 2 ký tự để so với "5x"
→ Chỉ cần duyệt i từ 0 đến 6 (tức là range(8 - 2 + 1) = range(7))
```

### 1.4. Code có comment từng dòng

```python
def tim_chuoi_con(doan_van, chuoi_can_tim):
    n = len(doan_van)          # Độ dài đoạn văn
    m = len(chuoi_can_tim)     # Độ dài chuỗi cần tìm
    vi_tri_tim_thay = []       # Lưu các vị trí tìm thấy

    # Duyệt từ vị trí 0 đến vị trí (n - m)
    # Vì từ vị trí (n - m + 1) trở đi không đủ ký tự để so sánh
    for i in range(n - m + 1):

        # Giả sử ban đầu là khớp
        da_khop = True

        # So sánh từng ký tự của chuỗi cần tìm
        for j in range(m):
            # So sánh ký tự thứ j của chuỗi cần tìm
            # với ký tự thứ (i + j) của đoạn văn
            if doan_van[i + j] != chuoi_can_tim[j]:
                da_khop = False   # Đánh dấu là không khớp
                break             # Dừng ngay, không cần so tiếp

        # Nếu sau khi so sánh xong mà vẫn khớp
        if da_khop == True:
            vi_tri_tim_thay.append(i)

    return vi_tri_tim_thay
```

### 1.5. Độ phức tạp

- **Trường hợp xấu nhất:** `O(n × m)` — phải so sánh tất cả ký tự.
- **Trường hợp tốt nhất:** `O(n)` — nếu ký tự đầu tiên đã lệch nhiều.

---

## Phần 2: Tách chuỗi thủ công (không dùng `split()`)

### 2.1. Bài toán

Cho dòng:

```text
"5x-123,106.7,10.8,17:30"
```

Cần tách thành 4 phần: `["5x-123", "106.7", "10.8", "17:30"]`.

### 2.2. Cách làm

Duyệt qua từng ký tự, gom vào biến tạm. Khi gặp dấu phẩy `,` thì lưu biến tạm vào kết quả và reset.

```text
Ký tự:  5  x  -  1  2  3  ,  1  0  6  .  7  ,  1  0  .  8  ,  1  7  :  3  0
                           ↑                 ↑                 ↑
                        GẶP DẤU ,        GẶP DẤU ,         GẶP DẤU ,
                        → Lưu "5x-123"   → Lưu "106.7"   → Lưu "10.8"
                        → Reset           → Reset          → Reset

Cuối cùng, lưu phần còn lại: "17:30"
```

### 2.3. Code

```python
def tach_chuoi_theo_dau_phay(line):
    ket_qua = []       # List lưu các phần tử đã tách
    chuoi_tam = ""     # Biến tạm để gom ký tự

    for i in range(len(line)):
        if line[i] == ',':
            # Gặp dấu phẩy → lưu chuỗi tạm vào kết quả
            ket_qua.append(chuoi_tam)
            chuoi_tam = ""   # Reset biến tạm
        else:
            # Chưa gặp dấu phẩy → gom ký tự vào biến tạm
            chuoi_tam = chuoi_tam + line[i]

    # Lưu phần cuối cùng (sau dấu phẩy cuối)
    ket_qua.append(chuoi_tam)

    return ket_qua
```

### 2.4. Ví dụ chạy thử

```python
line = "5x-123,106.7,10.8,17:30"
ket_qua = tach_chuoi_theo_dau_phay(line)
# ket_qua = ["5x-123", "106.7", "10.8", "17:30"]
```

---

## Phần 3: Tách giờ thủ công (không dùng `split(":")`)

### 3.1. Bài toán

Cho chuỗi thời gian: `"17:30"`. Cần lấy ra số giờ: `17`.

### 3.2. Cách làm

**Bước 1:** Tìm vị trí dấu `:`

```text
Chuỗi:  1  7  :  3  0
Index:  0  1  2  3  4
              ↑
         Tìm thấy dấu : tại index = 2
```

**Bước 2:** Lấy các ký tự từ đầu đến trước dấu `:`

```text
Ký tự cần lấy: '1' và '7' (index 0 và 1)
```

**Bước 3:** Chuyển chuỗi `"17"` thành số nguyên `17`

```text
Dùng mã ASCII:
ord('1') = 49, ord('0') = 48
→ '1' = 49 - 48 = 1
→ '7' = 55 - 48 = 7

Số = 1 × 10 + 7 = 17
```

### 3.3. Code

```python
def tach_gio(thoi_gian_str):
    # Bước 1: Tìm vị trí dấu ":"
    vi_tri_dau_hai_cham = -1
    for i in range(len(thoi_gian_str)):
        if thoi_gian_str[i] == ':':
            vi_tri_dau_hai_cham = i
            break

    # Bước 2: Lấy phần giờ (từ đầu đến trước dấu :)
    chuoi_gio = ""
    for i in range(vi_tri_dau_hai_cham):
        chuoi_gio = chuoi_gio + thoi_gian_str[i]

    # Bước 3: Chuyển chuỗi sang số nguyên
    gio = 0
    for i in range(len(chuoi_gio)):
        so = ord(chuoi_gio[i]) - ord('0')  # '1' → 1, '7' → 7
        gio = gio * 10 + so                 # 0*10+1=1, 1*10+7=17

    return gio
```

### 3.4. Ví dụ chạy thử

```python
thoi_gian = "17:30"
gio = tach_gio(thoi_gian)
# gio = 17

thoi_gian2 = "08:15"
gio2 = tach_gio(thoi_gian2)
# gio2 = 8
```

---

## Phần 4: Logic lọc và đếm xe

### 4.1. Điều kiện cần thỏa mãn

Một xe được đếm khi **đồng thời** thỏa 2 điều kiện:

| Điều kiện | Kiểm tra |
|-----------|----------|
| Thời gian từ 17h đến 19h | `17 <= gio < 19` |
| Biển số chứa `"5x"` | Dùng hàm `tim_chuoi_con()` trả về khác rỗng |

### 4.2. Flow xử lý từng dòng

```text
Đọc 1 dòng từ file
    ↓
Tách dấu phẩy → [bien_so, x, y, thoi_gian]
    ↓
Tách giờ từ thoi_gian → gio (số nguyên)
    ↓
Kiểm tra: 17 <= gio < 19 ?
    ├── KHÔNG → Bỏ qua, đọc dòng tiếp
    └── CÓ ↓
        Kiểm tra: bien_so có chứa "5x" ?
            ├── KHÔNG → Bỏ qua
            └── CÓ → ĐẾM +1, lưu vào danh sách
```

### 4.3. Code module chính

```python
def dem_xe_5x_gio_cao_diem(ten_file):
    dem = 0
    danh_sach_xe = []

    # Mở file
    file = open(ten_file, 'r')

    # Đọc từng dòng
    for line in file:
        # Loại bỏ ký tự xuống dòng
        line_sach = ""
        for i in range(len(line)):
            if line[i] != '\n' and line[i] != '\r':
                line_sach = line_sach + line[i]

        # Tách các trường
        cac_truong = tach_chuoi_theo_dau_phay(line_sach)

        # Kiểm tra có đủ 4 trường không
        if len(cac_truong) >= 4:
            bien_so = cac_truong[0]
            x = cac_truong[1]
            y = cac_truong[2]
            thoi_gian = cac_truong[3]

            # Tách giờ
            gio = tach_gio(thoi_gian)

            # Điều kiện 1: Giờ từ 17 đến 19
            if gio >= 17 and gio < 19:

                # Điều kiện 2: Biển số chứa "5x"
                vi_tri = tim_chuoi_con(bien_so, "5x")

                if len(vi_tri) > 0:
                    dem = dem + 1
                    danh_sach_xe.append((bien_so, x, y, thoi_gian))

    file.close()
    return dem, danh_sach_xe
```

---

## Phần 5: Ví dụ chạy toàn bộ

### File đầu vào `bienso_xe.txt`

```text
bien_so,x,y,thoi_gian
5x-1234,106.7,10.8,16:45
5x-5678,106.7,10.8,17:30
29A-1111,106.7,10.8,18:00
5x-9999,106.7,10.8,18:45
5x-0000,106.7,10.8,19:30
```

### Xử lý từng dòng

| Dòng | Biển số | Giờ | Giờ ∈ [17,19)? | Có "5x"? | Được đếm? |
|------|---------|-----|----------------|----------|-----------|
| 1 | 5x-1234 | 16 | ❌ (16 < 17) | ✅ | ❌ |
| 2 | 5x-5678 | 17 | ✅ | ✅ | ✅ |
| 3 | 29A-1111 | 18 | ✅ | ❌ | ❌ |
| 4 | 5x-9999 | 18 | ✅ | ✅ | ✅ |
| 5 | 5x-0000 | 19 | ❌ (19 ≥ 19) | ✅ | ❌ |

### Kết quả

```text
Tổng số xe '5x' từ 17h-19h: 2

Chi tiết:
  Biển số: 5x-5678 | Tọa độ: (106.7, 10.8) | Thời gian: 17:30
  Biển số: 5x-9999 | Tọa độ: (106.7, 10.8) | Thời gian: 18:45
```

---

## Tóm tắt các hàm đã viết

| Hàm | Chức năng | Thay thế hàm có sẵn |
|-----|-----------|---------------------|
| `tim_chuoi_con()` | Tìm chuỗi con trong đoạn văn | `str.find()`, `in`, `count()` |
| `tach_chuoi_theo_dau_phay()` | Tách chuỗi theo dấu `,` | `str.split(',')` |
| `tach_gio()` | Lấy giờ từ chuỗi `"HH:MM"` | `str.split(':')[0]`, `int()` |
| `dem_xe_5x_gio_cao_diem()` | Module chính đọc file và đếm | Kết hợp tất cả |
