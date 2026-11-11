# 🔄 Reverse Linked List — Đảo ngược danh sách liên kết

> Bài toán kinh điển về **thao tác con trỏ**: đảo ngược linked list với `O(n)` thời gian và `O(1)` bộ nhớ.

---

## 📋 Mục lục

- [1. Bài toán](#1-bài-toán)
- [2. Linked List là gì?](#2-linked-list-là-gì)
- [3. Ba cách giải](#3-ba-cách-giải)
- [4. Code Python đầy đủ](#4-code-python-đầy-đủ)
- [5. Chạy tay từng bước](#5-chạy-tay-từng-bước)
- [6. So sánh 3 cách](#6-so-sánh-3-cách)
- [7. Biến thể thường gặp](#7-biến-thể-thường-gặp)
- [8. Lỗi hay mắc](#8-lỗi-hay-mắc)
- [9. Bài học rút ra](#9-bài-học-rút-ra)

---

## 1. Bài toán

Cho `head` của một linked list. **Đảo ngược** list và trả về `head` mới.

### Ví dụ

```text
Input:  1 → 2 → 3 → 4 → 5 → None
Output: 5 → 4 → 3 → 2 → 1 → None

Input:  1 → 2 → None
Output: 2 → 1 → None

Input:  None (list rỗng)
Output: None
```

### Điều cốt lõi

Ta **không di chuyển giá trị**. Ta **đổi hướng các mũi tên `next`**.

```text
Trước:  [1] → [2] → [3] → None

Sau:    [1] ← [2] ← [3]
         ↑
        head mới = node 3
```

Mỗi node vẫn giữ nguyên `val`. Chỉ có `next` bị đổi hướng.

---

## 2. Linked List là gì?

### So sánh với Array

**Array** — các phần tử nằm **liền nhau** trong bộ nhớ:

```text
[8, 7, 2, 5]   ← truy cập bằng index: nums[0], nums[1]...
```

**Linked List** — các phần tử (**node**) nằm **rải rác**, mỗi node **giữ địa chỉ của node tiếp theo**:

```text
[8] → [7] → [2] → [5] → None
```

### Cấu trúc node

Mỗi node có 2 phần:
- **`val`**: giá trị (vd `8`)
- **`next`**: con trỏ tới node tiếp theo (hoặc `None` nếu là node cuối)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Đặc điểm quan trọng

| | Array | Linked List |
|---|---|---|
| Truy cập `nums[i]` | O(1) — nhảy thẳng | **O(n)** — phải đi từ đầu |
| Chèn/xóa ở giữa | O(n) — dời phần tử | **O(1)** — chỉ đổi `next` |
| Bộ nhớ | Liền nhau | Rải rác (tốn thêm chỗ cho `next`) |

**Điểm mấu chốt:** Linked List **không có index**. Muốn đảo ngược, ta **chỉ có thể đổi các con trỏ `next`** — không thể "sắp xếp lại vị trí" như array.

---

## 3. Ba cách giải

### 🐢 Cách 1 — Mảng phụ (dễ hiểu, tốn bộ nhớ)

1. Duyệt list, **chép tất cả giá trị** vào mảng.
2. Đảo ngược mảng.
3. Duyệt list lần nữa, **ghi đè giá trị** từ mảng đã đảo vào các node.

**Ưu điểm:** Dễ hiểu nhất.
**Nhược điểm:** Tốn `O(n)` bộ nhớ; không đúng tinh thần "đảo list".

### ⚡ Cách 2 — Ba con trỏ (chuẩn, O(1) bộ nhớ)

Duyệt list một lần. Tại mỗi node, **đổi hướng `next` về node trước**. Cần **3 con trỏ**:

| Con trỏ | Vai trò |
|---|---|
| `prev` | Node **trước** node hiện tại (ban đầu `None`) |
| `curr` | Node **hiện tại** đang xét (ban đầu `head`) |
| `next_node` | Node **tiếp theo** — giữ tạm để không mất đường |

**Ưu điểm:** `O(n)` thời gian, `O(1)` bộ nhớ — tối ưu nhất.
**Nhược điểm:** Cần hiểu con trỏ.

### 🔁 Cách 3 — Đệ quy (đẹp nhưng khó hiểu)

> "Đảo ngược list = đảo ngược phần đuôi, rồi gắn node đầu vào cuối."

**Ưu điểm:** Code ngắn, đẹp.
**Nhược điểm:** `O(n)` bộ nhớ do **ngăn xếp đệ quy** — có thể **stack overflow** với list lớn.

---

## 4. Code Python đầy đủ

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    """Tạo linked list từ mảng [1, 2, 3] → 1→2→3→None"""
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_list(head):
    """In list: 1 → 2 → 3 → None"""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" → ".join(vals) + " → None")


# ============================================================
# CÁCH 1: MẢNG PHỤ — O(n) thời gian, O(n) bộ nhớ
# ============================================================
def reverse_list_array(head):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next

    values.reverse()

    node = head
    i = 0
    while node:
        node.val = values[i]
        i += 1
        node = node.next

    return head


# ============================================================
# CÁCH 2: LẶP — O(n) thời gian, O(1) bộ nhớ (KHUYÊN DÙNG)
# ============================================================
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next    # 1. giữ đường đi
        curr.next = prev         # 2. đảo hướng
        prev = curr              # 3. prev tiến
        curr = next_node         # 4. curr tiến

    return prev


# ============================================================
# CÁCH 3: ĐỆ QUY — O(n) thời gian, O(n) bộ nhớ (stack)
# ============================================================
def reverse_list_recursive(head):
    if not head or not head.next:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# ============================================================
# CHẠY THỬ
# ============================================================
if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    print("Trước:  ", end="")
    print_list(head)
    head = reverse_list(head)
    print("Sau:    ", end="")
    print_list(head)

    head = build_list([1, 2])
    print("\nTrước:  ", end="")
    print_list(head)
    head = reverse_list(head)
    print("Sau:    ", end="")
    print_list(head)

    head = build_list([])
    print("\nTrước:  ", end="")
    print_list(head)
    head = reverse_list(head)
    print("Sau:    ", end="")
    print_list(head)

    head = build_list([1, 2, 3])
    print("\nĐệ quy trước:  ", end="")
    print_list(head)
    head = reverse_list_recursive(head)
    print("Đệ quy sau:    ", end="")
    print_list(head)
```

**Kết quả:**

```text
Trước:   1 → 2 → 3 → 4 → 5 → None
Sau:     5 → 4 → 3 → 2 → 1 → None

Trước:   1 → 2 → None
Sau:     2 → 1 → None

Trước:   → None
Sau:     → None

Đệ quy trước:   1 → 2 → 3 → None
Đệ quy sau:     3 → 2 → 1 → None
```

---

## 5. Chạy tay từng bước

Ví dụ: `1 → 2 → 3 → None`

### Ban đầu

```text
prev = None
curr = [1]

None    [1] → [2] → [3] → None
 ↑      ↑
prev   curr
```

### Bước 1 — xét node `1`

```text
1. next_node = curr.next = [2]
2. curr.next = prev = None         → [1] trỏ về None
3. prev = curr = [1]
4. curr = next_node = [2]
```

```text
None ← [1]    [2] → [3] → None
        ↑      ↑
       prev   curr
```

### Bước 2 — xét node `2`

```text
1. next_node = curr.next = [3]
2. curr.next = prev = [1]          → [2] trỏ về [1]
3. prev = curr = [2]
4. curr = next_node = [3]
```

```text
None ← [1] ← [2]    [3] → None
               ↑      ↑
              prev   curr
```

### Bước 3 — xét node `3`

```text
1. next_node = curr.next = None
2. curr.next = prev = [2]          → [3] trỏ về [2]
3. prev = curr = [3]
4. curr = next_node = None
```

```text
None ← [1] ← [2] ← [3]
                     ↑
                    prev (head mới)

curr = None → vòng lặp dừng
```

### ✅ Kết quả: `None ← 1 ← 2 ← 3`, head mới = `3`

Viết xuôi lại: `3 → 2 → 1 → None`. Đúng!

---

## 6. So sánh 3 cách

| | Cách 1 (mảng phụ) | Cách 2 (lặp) | Cách 3 (đệ quy) |
|---|---|---|---|
| **Thời gian** | O(n) | **O(n)** | O(n) |
| **Bộ nhớ thêm** | O(n) | **O(1)** ⭐ | O(n) — stack đệ quy |
| **Độ khó** | Dễ | Trung bình | Khó |
| **Dùng trong phỏng vấn** | ❌ | ✅ **Chuẩn** | ✅ (nếu giải thích được) |
| **An toàn với list lớn** | ✅ | ✅ | ❌ stack overflow |

**→ Mặc định chọn Cách 2.** Chỉ dùng Cách 3 nếu được hỏi "có cách đệ quy không?".

---

## 7. Biến thể thường gặp

Đây là những bài **dùng lại đúng mẹo "3 con trỏ"** của bài này. Học một lần → giải được cả họ.

### Biến thể 1: Đảo ngược đoạn `[m, n]`

> Cho `head`, đảo ngược chỉ các node từ vị trí `m` đến `n`. (LeetCode 92)

**Ý tưởng:** tìm node trước vị trí `m`, áp dụng đảo 3 con trỏ cho đoạn `[m, n]`, rồi nối lại.

### Biến thể 2: Đảo ngược theo nhóm `k` node

> `1→2→3→4→5`, k=2 → `2→1→4→3→5`

**Ý tưởng:** lặp lại "đảo k node" cho từng nhóm.

### Biến thể 3: Kiểm tra Palindrome Linked List

> `1→2→2→1` → true

**Ý tưởng:** tìm giữa list → đảo nửa sau → so sánh 2 nửa.

### Biến thể 4: Cộng 2 số biểu diễn bằng Linked List

> `(2→4→3)` + `(5→6→4)` = `(7→0→8)` (342 + 465 = 807)

**Ý tưởng:** đảo list trước (hoặc dùng đệ quy) để cộng từ hàng đơn vị.

### 💡 Nhận diện pattern

Khi nào bài toán nói **"đảo ngược"**, **"so sánh từ cuối"**, **"cộng từ hàng đơn vị"** trên Linked List → **nghĩ ngay đến mẹo 3 con trỏ**.

---

## 8. Lỗi hay mắc

| Lỗi | Hậu quả | Cách sửa |
|---|---|---|
| Quên lưu `next_node` trước khi đảo | Mất node tiếp, list bị cắt cụt | Lưu `next_node` **trước** khi đảo |
| Trả về `head` cũ | Trả về node cuối (sai) | Trả về `prev` (head mới) |
| Không xử lý list rỗng / 1 node | Crash hoặc sai | `if not head: return None` |
| Dùng đệ quy cho list lớn | Stack overflow | Dùng cách lặp |
| Đảo `curr.next` trước khi lưu `next` | Mất đường đi tiếp | **Thứ tự 4 bước quan trọng** |

### ⚠️ Thứ tự 4 bước không được đổi

```python
next_node = curr.next    # 1. PHẢI làm trước — giữ đường đi
curr.next = prev         # 2. đảo hướng
prev = curr              # 3. prev tiến
curr = next_node         # 4. curr tiến
```

Nếu đảo bước 2 trước bước 1 → **mất node tiếp theo** → không đi tiếp được.

---

## 9. Bài học rút ra

### 💡 Ba điều cốt lõi

1. **Linked List không có index** — chỉ đảo được bằng cách **đổi con trỏ `next`**, không "sắp xếp lại vị trí".

2. **Thứ tự 4 bước không được đổi:**
   `lưu next → đảo curr.next → prev tiến → curr tiến`.

3. **Đảo list = dùng 3 con trỏ `prev, curr, next_node`.** Đây là **khuôn mẫu (pattern)** lặp lại trong hàng chục bài toán khác.

### 🎯 Tóm gọn bằng 3 câu

1. **Bài toán:** đảo ngược linked list bằng cách đổi hướng các con trỏ `next`.
2. **Cách chuẩn:** dùng 3 con trỏ `prev, curr, next_node` — `O(n)` thời gian, `O(1)` bộ nhớ.
3. **Mẹo cốt lõi:** luôn **lưu `next` trước khi đảo `curr.next`** — nếu không sẽ mất đường.

---

## 📚 Tham khảo

- [LeetCode 206 — Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [LeetCode 92 — Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- [GeeksforGeeks — Reverse a Linked List](https://www.geeksforgeeks.org/reverse-a-linked-list/)

---

## 📝 License

MIT — tự do sử dụng, chỉnh sửa, chia sẻ.
