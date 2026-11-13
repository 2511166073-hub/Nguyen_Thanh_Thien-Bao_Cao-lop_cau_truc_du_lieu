# BÁO CÁO: BÀI TOÁN KNAPSACK BẰNG QUY HOẠCH ĐỘNG (Knapsack DP)

## Mục lục

1. [Tổng quan bài toán](#1-tổng-quan-bài-toán)
2. [Phân loại Knapsack](#2-phân-loại-knapsack)
3. [Knapsack 0/1 — Ý tưởng và công thức](#3-knapsack-01--ý-tưởng-và-công-thức)
4. [Minh họa từng bước](#4-minh-họa-từng-bước)
5. [Cài đặt Python — Knapsack 0/1](#5-cài-đặt-python--knapsack-01)
6. [Tối ưu bộ nhớ — mảng 1 chiều](#6-tối-ưu-bộ-nhớ--mảng-1-chiều)
7. [Knapsack không giới hạn (Unbounded)](#7-knapsack-không-giới-hạn-unbounded)
8. [Knapsack phân số (Fractional)](#8-knapsack-phân-số-fractional)
9. [Truy vết các vật được chọn](#9-truy-vết-các-vật-được-chọn)
10. [Độ phức tạp](#10-độ-phức-tạp)
11. [So sánh các biến thể](#11-so-sánh-các-biến-thể)
12. [Lỗi thường gặp](#12-lỗi-thường-gặp)
13. [Ứng dụng thực tế](#13-ứng-dụng-thực-tế)
14. [Kết luận](#14-kết-luận)

---

## 1. Tổng quan bài toán

### 1.1. Phát biểu

Cho `n` vật, mỗi vật có:
- **Trọng lượng** `w[i]`
- **Giá trị** `v[i]`

Và một **cái túi** có sức chứa tối đa `W`.

**Yêu cầu:** Chọn một tập con các vật sao cho:
- **Tổng trọng lượng ≤ W**
- **Tổng giá trị là lớn nhất**

### 1.2. Ví dụ

```
n = 4 vật:
Vật 1: w=1, v=1
Vật 2: w=3, v=4
Vật 3: w=4, v=5
Vật 4: w=5, v=7
W = 7

Chọn: vật 2 (w=3, v=4) + vật 3 (w=4, v=5) → tổng w=7, v=9
Hoặc: vật 1 + vật 3 → w=5, v=6
Hoặc: vật 2 + vật 4 → w=8 > W → không được
→ Đáp án:  (chọn vật 2 và 3)
```

### 1.3. Vì sao cần DP?

**Thử vét cạn:** có `2^n` tập con → với `n = 40` đã là `~10^12` → **quá chậm**.

**Tham lam (greedy):** chọn theo tỉ lệ `v/w` cao nhất → **không tối ưu** cho Knapsack 0/1.

**DP:** giải trong `O(nW)` — đánh đổi giữa thời gian và bộ nhớ.

---

## 2. Phân loại Knapsack

| Loại | Đặc điểm | Cách giải |
|------|-----------|-----------|
| **0/1 Knapsack** | Mỗi vật **chọn hoặc không** (1 lần) | DP — bảng 2 chiều hoặc 1 chiều |
| **Unbounded Knapsack** | Mỗi vật được chọn **nhiều lần** | DP — mảng 1 chiều, duyệt xuôi |
| **Fractional Knapsack** | Được chọn **một phần** vật (chia nhỏ) | **Greedy** — sắp theo `v/w` |

> **Lưu ý:** Chỉ **Knapsack 0/1** và **Unbounded** mới cần DP. **Fractional** dùng greedy là đủ tối ưu.

---

## 3. Knapsack 0/1 — Ý tưởng và công thức

### 3.1. Định nghĩa trạng thái

> `dp[i][j]` = **giá trị lớn nhất** có thể đạt được khi xét **`i` vật đầu tiên** (từ `1` đến `i`) với **sức chứa `j`**.

- `i` chạy từ `0` đến `n`
- `j` chạy từ `0` đến `W`

### 3.2. Công thức truy hồi

Với vật thứ `i` (1-indexed), trọng lượng `w[i]`, giá trị `v[i]`:

```
Nếu w[i] > j:                              ← không đủ chỗ chứa vật i
    dp[i][j] = dp[i-1][j]                  ← bỏ vật i

Nếu w[i] <= j:                             ← đủ chỗ → có 2 lựa chọn
    dp[i][j] = max(
        dp[i-1][j],                        ← KHÔNG chọn vật i
        dp[i-1][j - w[i]] + v[i]           ← CHỌN vật i
    )
```

### 3.3. Điều kiện cơ sở

```
dp[0][j] = 0    với mọi j      ← không có vật nào → giá trị 0
dp[i][0] = 0    với mọi i      ← sức chứa 0 → không chọn được gì
```

### 3.4. Đáp án

```
dp[n][W]
```

### 3.5. Giải thích trực quan

Tại mỗi ô `(i, j)`, ta đứng trước **2 lựa chọn**:

```
                        dp[i][j]
                       /         \
              Bỏ vật i           Chọn vật i
                 |                   |
           dp[i-1][j]      dp[i-1][j-w[i]] + v[i]
        (giữ nguyên         (lấy giá trị tốt nhất
         kết quả cũ)         khi còn j-w[i] chỗ,
                              cộng thêm v[i])
```

→ Chọn nhánh **max**. Đó là bản chất **quy hoạch động**: chia bài toán lớn thành bài toán con nhỏ hơn, lưu kết quả để tái sử dụng.

---

## 4. Minh họa từng bước

### 4.1. Dữ liệu

```
n = 4
w = [_, 1, 3, 4, 5]      (1-indexed)
v = [_, 1, 4, 5, 7]
W = 7
```

### 4.2. Bảng DP `dp[i][j]`

| `i \ j` | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** |
|---------|-------|-------|-------|-------|-------|-------|-------|-------|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** (w=1,v=1) | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **2** (w=3,v=4) | 0 | 1 | 1 | 4 | 5 | 5 | 5 | 5 |
| **3** (w=4,v=5) | 0 | 1 | 1 | 4 | 5 | 6 | 6 | 9 |
| **4** (w=5,v=7) | 0 | 1 | 1 | 4 | 5 | 7 | 8 | 9 |

**Đáp án:** `dp[4][7] = 9` ✅

### 4.3. Giải thích vài ô tiêu biểu

**Ô `dp[1][1]`** (vật 1, W=1):
- `w[1]=1 ≤ 1` → `max(dp[0][1], dp[0][0]+1) = max(0, 1) = 1`

**Ô `dp[2][3]`** (vật 1-2, W=3):
- `w[2]=3 ≤ 3` → `max(dp[1][3], dp[1][0]+4) = max(1, 4) = 4` (chọn vật 2)

**Ô `dp[3][7]`** (vật 1-3, W=7):
- `w[3]=4 ≤ 7` → `max(dp[2][7], dp[2][3]+5) = max(5, 4+5) = 9` (chọn vật 2 + vật 3)

**Ô `dp[4][7]`** (vật 1-4, W=7):
- `w[4]=5 ≤ 7` → `max(dp[3][7], dp[3][2]+7) = max(9, 1+7) = 9` (không chọn vật 4, giữ 9)

### 4.4. Truy vết ngược

Bắt đầu từ `dp[4][7] = 9`:

| Bước | Ô | So sánh | Kết luận |
|------|---|---------|----------|
| 1 | `dp[4][7]=9` vs `dp[3][7]=9` | Bằng nhau → **không chọn vật 4** | Đi lên `dp[3][7]` |
| 2 | `dp[3][7]=9` vs `dp[2][7]=5` | Khác → **chọn vật 3** | Đi chéo `dp[2][7-4]=dp[2][3]` |
| 3 | `dp[2][3]=4` vs `dp[1][3]=1` | Khác → **chọn vật 2** | Đi chéo `dp[1][3-3]=dp[1][0]` |
| 4 | `dp[1][0]=0` | j=0 → dừng | — |

→ **Các vật được chọn:** vật 2 (w=3,v=4) + vật 3 (w=4,v=5) = **9**. ✅

---

## 5. Cài đặt Python — Knapsack 0/1

### 5.1. Bảng 2 chiều (dễ hiểu, dễ truy vết)

```python
def knapsack_01(w, v, W):
    """
    w: list trọng lượng (0-indexed)
    v: list giá trị (0-indexed)
    W: sức chứa
    """
    n = len(w)
    # dp[i][j] = giá trị max khi xét i vật đầu, sức chứa j
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        wi = w[i - 1]     # 1-indexed → 0-indexed
        vi = v[i - 1]
        for j in range(W + 1):
            if wi > j:
                dp[i][j] = dp[i - 1][j]                 # không đủ chỗ
            else:
                dp[i][j] = max(
                    dp[i - 1][j],                       # bỏ vật i
                    dp[i - 1][j - wi] + vi              # chọn vật i
                )
    return dp[n][W]
```

**Chạy thử:**

```python
w = [1, 3, 4, 5]
v = [1, 4, 5, 7]
W = 7

print(knapsack_01(w, v, W))     # 9
```

### 5.2. Kiểm tra bảng DP

```python
def knapsack_01_verbose(w, v, W):
    n = len(w)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(W + 1):
            if w[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])

    # In bảng
    for row in dp:
        print(row)
    return dp[n][W]

# Output:
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 4, 5, 5, 5, 5]
# [0, 1, 1, 4, 5, 6, 6, 9]
# [0, 1, 1, 4, 5, 7, 8, 9]
```

---

## 6. Tối ưu bộ nhớ — mảng 1 chiều

### 6.1. Quan sát

Công thức `dp[i][j]` chỉ phụ thuộc vào **dòng `i-1`** (dòng ngay trên). Không cần lưu toàn bộ bảng → **giảm từ `O(nW)` xuống `O(W)`**.

### 6.2. Công thức 1 chiều

```
dp[j] = max(dp[j], dp[j - w[i]] + v[i])
```

### 6.3. Điểm mấu chốt: **duyệt `j` NGƯỢC**

> **Bắt buộc duyệt `j` từ `W` về `0`** (giảm dần), không phải từ `0` đến `W`.

**Vì sao?** Vì `dp[j]` mới phụ thuộc `dp[j - w[i]]` — mà `j - w[i] < j`. Nếu duyệt **xuôi**, `dp[j - w[i]]` có thể đã bị **cập nhật bởi chính vật `i`** → **vô tình chọn vật `i` nhiều lần** → thành **Unbounded Knapsack**, không còn là 0/1.

**Minh họa sai:** duyệt xuôi với vật `i` có `w=1, v=1`, `W=3`:

```
dp = [0, 0, 0, 0]

j=1: dp[1] = max(dp[1], dp[0]+1) = 1
j=2: dp[2] = max(dp[2], dp[1]+1) = 2    ← dùng dp[1] VỪA CẬP NHẬT → chọn vật i 2 lần!
j=3: dp[3] = max(dp[3], dp[2]+1) = 3    ← chọn vật i 3 lần!
```

→ Kết quả `3` — tức chọn vật `i` 3 lần → **SAI** cho 0/1.

**Duyệt ngược:**

```
dp = [0, 0, 0, 0]

j=3: dp[3] = max(dp[3], dp[2]+1) = max(0, 0+1) = 1
j=2: dp[2] = max(dp[2], dp[1]+1) = max(0, 0+1) = 1
j=1: dp[1] = max(dp[1], dp[0]+1) = max(0, 0+1) = 1
```

→ Kết quả `1` — chọn vật `i` đúng 1 lần ✅

### 6.4. Cài đặt

```python
def knapsack_01_1d(w, v, W):
    n = len(w)
    dp = [0] * (W + 1)

    for i in range(n):
        wi, vi = w[i], v[i]
        for j in range(W, wi - 1, -1):     # ← NGƯỢC
            dp[j] = max(dp[j], dp[j - wi] + vi)

    return dp[W]
```

**Chạy thử:**

```python
w = [1, 3, 4, 5]
v = [1, 4, 5, 7]
W = 7
print(knapsack_01_1d(w, v, W))    # 9
```

### 6.5. Bảng so sánh

| Cách | Bộ nhớ | Duyệt `j` | Truy vết được? |
|------|--------|-----------|----------------|
| **2 chiều** | `O(nW)` | Bất kỳ | ✅ Có |
| **1 chiều** | `O(W)` | **Ngược** (W → 0) | ❌ Không (mất thông tin) |
| **1 chiều + mảng phụ** | `O(W)` | Ngược | ✅ Có (dùng thêm `parent[]`) |

---

## 7. Knapsack không giới hạn (Unbounded)

### 7.1. Khác biệt

- **0/1:** mỗi vật chọn **tối đa 1 lần**
- **Unbounded:** mỗi vật chọn **bao nhiêu lần cũng được**

### 7.2. Công thức

```
dp[j] = max(dp[j], dp[j - w[i]] + v[i])
```

**Giống hệt 0/1**, chỉ khác **chiều duyệt `j`**:

| Loại | Duyệt `j` |
|------|-----------|
| **0/1** | **Ngược** `W → w[i]` |
| **Unbounded** | **Xuôi** `w[i] → W` |

### 7.3. Vì sao duyệt xuôi cho Unbounded?

Duyệt xuôi → `dp[j - w[i]]` **đã được cập nhật bởi vật `i`** → cho phép chọn vật `i` nhiều lần. Đó chính là điều Unbounded muốn.

**Minh họa:** vật `w=1, v=1`, `W=3`:

```
dp = [0, 0, 0, 0]

j=1: dp[1] = max(0, dp[0]+1) = 1
j=2: dp[2] = max(0, dp[1]+1) = 2    ← dùng dp[1] vừa cập nhật → chọn 2 lần
j=3: dp[3] = max(0, dp[2]+1) = 3    ← chọn 3 lần
```

→ Kết quả `3` — đúng cho Unbounded ✅

### 7.4. Cài đặt

```python
def knapsack_unbounded(w, v, W):
    dp = [0] * (W + 1)

    for i in range(len(w)):
        wi, vi = w[i], v[i]
        for j in range(wi, W + 1):          # ← XUÔI
            dp[j] = max(dp[j], dp[j - wi] + vi)

    return dp[W]
```

**Ví dụ:** `w=[1,3,4,5]`, `v=[1,4,5,7]`, `W=7`:

```
dp = [0, 1, 2, 4, 5, 7, 8, 9]   → dp[7] = 9
```

Với Unbounded, chọn vật 2 (w=3,v=4) **2 lần** + vật 1 (w=1,v=1) **1 lần** → w=7, v=9. Hoặc các cách khác cho cùng kết quả.

---

## 8. Knapsack phân số (Fractional)

### 8.1. Đặc điểm

Được chọn **một phần** vật — ví dụ chọn 0.5 kg vàng từ túi 1 kg. **Không cần DP** — **greedy** là tối ưu.

### 8.2. Ý tưởng

1. Tính tỉ lệ `v[i] / w[i]` cho từng vật.
2. **Sắp xếp giảm dần** theo tỉ lệ.
3. Lần lượt chọn vật có tỉ lệ cao nhất; nếu không đủ chỗ → chọn **một phần** vừa đủ lấp đầy túi.

### 8.3. Cài đặt

```python
def knapsack_fractional(w, v, W):
    items = sorted(
        [(v[i] / w[i], w[i], v[i]) for i in range(len(w))],
        reverse=True
    )

    total_value = 0.0
    for ratio, wi, vi in items:
        if W >= wi:
            total_value += vi
            W -= wi
        else:
            total_value += ratio * W     # chọn một phần
            break

    return total_value
```

**Chạy thử:**

```python
w = [1, 3, 4, 5]
v = [1, 4, 5, 7]
W = 7
print(knapsack_fractional(w, v, W))   # 9.0
```

### 8.4. Vì sao greedy tối ưu cho Fractional?

Vì có thể **chia nhỏ** vật → luôn lấp đầy túi bằng phần có tỉ lệ cao nhất còn lại. Không có "lãng phí" chỗ trống.

**Phản ví dụ cho 0/1 (greedy thất bại):**

```
Vật A: w=10, v=60  (ratio 6.0)
Vật B: w=20, v=100 (ratio 5.0)
Vật C: w=30, v=120 (ratio 4.0)
W = 50

Greedy: chọn A (10) + B (20) + C (30) = 60 → w=50? Không, 10+20+30=60 > 50
       Chọn A + B = w=30, v=160
       Còn 20 chỗ, không chọn được C (w=30 > 20)
       → Kết quả greedy: 160

Tối ưu: B + C = w=50, v=220  ← tốt hơn!
```

→ **0/1 cần DP**, không thể greedy.

---

## 9. Truy vết các vật được chọn

### 9.1. Dùng bảng 2 chiều

```python
def knapsack_01_with_trace(w, v, W):
    n = len(w)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if w[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])

    # Truy vết ngược
    chosen = []
    j = W
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:       # có thay đổi → vật i được chọn
            chosen.append(i - 1)          # lưu index 0-based
            j -= w[i-1]

    chosen.reverse()
    return dp[n][W], chosen


w = [1, 3, 4, 5]
v = [1, 4, 5, 7]
W = 7
val, items = knapsack_01_with_trace(w, v, W)
print(f"Giá trị max: {val}")           # 9
print(f"Vật chọn (0-indexed): {items}")  # [1, 2]
```

### 9.2. Dùng mảng 1 chiều + mảng `parent`

```python
def knapsack_01_1d_trace(w, v, W):
    dp = [0] * (W + 1)
    parent = [-1] * (W + 1)       # parent[j] = vật cuối cùng được thêm vào để đạt dp[j]

    for i in range(len(w)):
        for j in range(W, w[i] - 1, -1):
            if dp[j - w[i]] + v[i] > dp[j]:
                dp[j] = dp[j - w[i]] + v[i]
                parent[j] = i

    # Truy vết
    chosen = []
    j = W
    while j > 0 and parent[j] != -1:
        i = parent[j]
        chosen.append(i)
        j -= w[i]

    chosen.reverse()
    return dp[W], chosen
```

---

## 10. Độ phức tạp

### 10.1. Knapsack 0/1

| Cách | Thời gian | Bộ nhớ |
|------|-----------|--------|
| **2 chiều** | `O(nW)` | `O(nW)` |
| **1 chiều** | `O(nW)` | `O(W)` |
| **1 chiều + parent** | `O(nW)` | `O(W)` |

### 10.2. Knapsack Unbounded

| Cách | Thời gian | Bộ nhớ |
|------|-----------|--------|
| **1 chiều** | `O(nW)` | `O(W)` |

### 10.3. Knapsack Fractional

| Bước | Thời gian |
|------|-----------|
| Sắp xếp | `O(n log n)` |
| Duyệt | `O(n)` |
| **Tổng** | **`O(n log n)`** |

### 10.4. So sánh với vét cạn

| `n` | `2^n` (vét cạn) | `nW` (DP, W=1000) |
|-----|-----------------|-------------------|
| 10 | 1,024 | 10,000 |
| 20 | ~1 triệu | 20,000 |
| 30 | ~1 tỷ | 30,000 |
| 40 | ~1 nghìn tỷ | 40,000 |
| **100** | **Không tưởng** | **100,000** ⚡ |

→ **DP thắng vét cạn** ngay từ `n ≈ 20`.

### 10.5. Lưu ý về `W` lớn

`O(nW)` là **pseudo-polynomial** — phụ thuộc vào **giá trị** `W`, không chỉ `n`. Nếu `W = 10^9` → `O(nW)` quá lớn → cần cách khác (meet-in-the-middle, DP theo giá trị, nhánh cận).

---

## 11. So sánh các biến thể

| Tiêu chí | 0/1 | Unbounded | Fractional |
|----------|-----|-----------|------------|
| **Mỗi vật chọn** | 0 hoặc 1 lần | Nhiều lần | Một phần |
| **Cách giải** | DP | DP | Greedy |
| **Duyệt `j`** | **Ngược** | **Xuôi** | — |
| **Thời gian** | `O(nW)` | `O(nW)` | `O(n log n)` |
| **Bộ nhớ** | `O(W)` | `O(W)` | `O(n)` |
| **Tối ưu?** | ✅ | ✅ | ✅ (greedy) |

**Mẹo nhớ:**

```
0/1        → j chạy NGƯỢC (W → w[i])   → mỗi vật dùng 1 lần
Unbounded  → j chạy XUÔI (w[i] → W)    → mỗi vật dùng nhiều lần
Fractional → sort theo v/w giảm dần     → greedy
```

---

## 12. Lỗi thường gặp

### 12.1. Duyệt `j` xuôi cho Knapsack 0/1

```python
# ❌ SAI — thành Unbounded
for j in range(wi, W + 1):
    dp[j] = max(dp[j], dp[j - wi] + vi)

# ✅ ĐÚNG
for j in range(W, wi - 1, -1):
    dp[j] = max(dp[j], dp[j - wi] + vi)
```

### 12.2. Nhầm index 0-based và 1-based

```python
# Với w, v là 0-indexed:
for i in range(1, n + 1):
    wi = w[i - 1]     # ← phải trừ 1
    vi = v[i - 1]
```

### 12.3. Khởi tạo sai

```python
# ❌ SAI — khởi tạo -1 có thể gây lỗi khi cộng
dp = [[-1] * (W + 1) for _ in range(n + 1)]

# ✅ ĐÚNG — giá trị 0 là an toàn (không chọn gì = 0)
dp = [[0] * (W + 1) for _ in range(n + 1)]
```

### 12.4. Quên trường hợp `w[i] > j`

```python
# ❌ SAI — không kiểm tra, có thể index âm
dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i-1]] + v[i-1])
# Nếu j - w[i-1] < 0 → index âm trong Python không lỗi nhưng sai logic

# ✅ ĐÚNG
if w[i-1] > j:
    dp[i][j] = dp[i-1][j]
else:
    dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i-1]] + v[i-1])
```

### 12.5. Nhầm Knapsack 0/1 với Fractional

```python
# ❌ SAI — dùng greedy cho 0/1
items.sort(key=lambda x: x[1]/x[0], reverse=True)
# → Có thể cho kết quả không tối ưu (xem phản ví dụ mục 8.4)

# ✅ ĐÚNG — 0/1 phải dùng DP
```

### 12.6. Quên truy vết khi cần in vật được chọn

```python
# ❌ Chỉ trả về giá trị — không biết chọn vật nào
return dp[n][W]

# ✅ Trả về cả danh sách vật
return dp[n][W], chosen_items
```

---

## 13. Ứng dụng thực tế

| Lĩnh vực | Bài toán |
|----------|----------|
| **Tài chính** | Chọn danh mục đầu tư tối ưu với ngân sách hạn chế |
| **Logistics** | Xếp hàng vào container/ xe tải có tải trọng giới hạn |
| **Lập lịch** | Chọn task có lợi nhuận cao nhất trong thời gian hạn chế |
| **Mật mã** | Knapsack cryptosystem (Merkle–Hellman) |
| **Machine Learning** | Feature selection với chi phí tính toán |
| **Cloud** | Chọn VM/container tối ưu chi phí |
| **Game** | Chọn item/trang bị tối ưu cho nhân vật |

---

## 14. Kết luận

> **Knapsack 0/1 = quy hoạch động trên bảng `dp[i][j]`, mỗi vật có 2 lựa chọn (bỏ hoặc chọn), lấy `max`. Tối ưu bộ nhớ bằng mảng 1 chiều — nhớ duyệt `j` NGƯỢC.**

**Tóm tắt các ý chính:**

| Ý | Nội dung |
|---|----------|
| **Trạng thái** | `dp[i][j]` = giá trị max khi xét `i` vật đầu, sức chứa `j` |
| **Công thức** | `dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])` |
| **Cơ sở** | `dp[0][j] = dp[i][0] = 0` |
| **Đáp án** | `dp[n][W]` |
| **Tối ưu bộ nhớ** | Mảng 1 chiều, duyệt `j` **ngược** cho 0/1 |
| **Unbounded** | Duyệt `j` **xuôi** |
| **Fractional** | Greedy — sort theo `v/w` giảm dần |
| **Độ phức tạp** | `O(nW)` thời gian, `O(W)` bộ nhớ (1 chiều) |
| **Truy vết** | So sánh `dp[i][j]` với `dp[i-1][j]` — khác → chọn vật `i` |

**Câu chốt để nhớ:**

```
Knapsack 0/1        → DP, j NGƯỢC
Knapsack Unbounded  → DP, j XUÔI
Knapsack Fractional → Greedy, sort v/w
```

**Code "phỏng vấn" (1 chiều, tối ưu):**

```python
def knapsack_01(w, v, W):
    dp = [0] * (W + 1)
    for i in range(len(w)):
        for j in range(W, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    return dp[W]
```
