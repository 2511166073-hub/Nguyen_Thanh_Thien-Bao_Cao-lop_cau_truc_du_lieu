# BÁO CÁO: TÌM PHẦN TỬ LỚN THỨ K BẰNG HEAP (Kth Largest — Heap)

## Mục lục

1. [Tổng quan bài toán](#1-tổng-quan-bài-toán)
2. [Ý tưởng cốt lõi — Min-Heap kích thước K](#2-ý-tưởng-cốt-lõi--min-heap-kích-thước-k)
3. [Minh họa từng bước](#3-minh-họa-từng-bước)
4. [Cài đặt Python](#4-cài-đặt-python)
5. [Vì sao dùng Min-Heap mà không dùng Max-Heap?](#5-vì-sao-dùng-min-heap-mà-không-dùng-max-heap)
6. [So sánh các cách giải](#6-so-sánh-các-cách-giải)
7. [Độ phức tạp](#7-độ-phức-tạp)
8. [Biến thể: Kth Smallest](#8-biến-thể-kth-smallest)
9. [Biến thể: K phần tử lớn nhất](#9-biến-thể-k-phần-tử-lớn-nhất)
10. [Lỗi thường gặp](#10-lỗi-thường-gặp)
11. [Kết luận](#11-kết-luận)

---

## 1. Tổng quan bài toán

### 1.1. Đề bài (LeetCode 215 — Kth Largest Element in an Array)

Cho một mảng số nguyên `nums` và số nguyên `k`. Tìm **phần tử lớn thứ `k`** trong mảng.

**Lưu ý:** "lớn thứ k" tính theo **thứ tự giảm dần**, không phải thứ tự tăng dần.

### 1.2. Ví dụ

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
# Output: 5
# Vì sắp giảm dần: [6, 5, 4, 3, 2, 1] → phần tử thứ 2 là 5
```

```python
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
# Output: 4
# Vì sắp giảm dần: [6, 5, 5, 4, 3, 3, 2, 2, 1] → phần tử thứ 4 là 4
```

### 1.3. Các cách giải

| Cách | Ý tưởng | Thời gian | Bộ nhớ |
|------|---------|-----------|--------|
| **Sort** | Sắp xếp toàn bộ rồi lấy `nums[-k]` | `O(n log n)` | `O(1)` hoặc `O(n)` |
| **Min-Heap k phần tử** | Giữ heap k phần tử lớn nhất | `O(n log k)` | `O(k)` |
| **Quickselect** | Chọn ngẫu nhiên pivot, chia mảng | Trung bình `O(n)`, xấu `O(n²)` | `O(1)` |

→ **Heap là cách cân bằng tốt nhất** giữa tốc độ và độ đơn giản, đặc biệt khi `k` nhỏ và dữ liệu lớn (stream).

---

## 2. Ý tưởng cốt lõi — Min-Heap kích thước K

### 2.1. Ý tưởng

> **Duy trì một Min-Heap chứa đúng `k` phần tử lớn nhất đã gặp.**
> Khi duyệt hết mảng, **đỉnh heap (phần tử nhỏ nhất trong heap)** chính là **phần tử lớn thứ `k`** của toàn mảng.

### 2.2. Vì sao đỉnh heap là đáp án?

- Heap chứa `k` phần tử **lớn nhất** trong toàn bộ mảng.
- Trong `k` phần tử đó, **phần tử nhỏ nhất** chính là phần tử **lớn thứ `k`** của mảng.
- Min-Heap đặt phần tử nhỏ nhất ở **đỉnh** → `heap[0]` là đáp án.

**Ví dụ minh họa:** `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`

Khi duyệt hết, heap chứa 2 phần tử lớn nhất: `[5, 6]` (dạng min-heap: `[5, 6]` với `5` ở đỉnh).

→ `heap[0] = 5` = phần tử lớn thứ 2. ✅

### 2.3. Thuật toán

```
function findKthLargest(nums, k):
    heap = empty min-heap

    for num in nums:
        heap.push(num)                  # đưa num vào heap
        if len(heap) > k:
            heap.pop()                  # loại phần tử nhỏ nhất

    return heap[0]                       # đỉnh heap = đáp án
```

### 2.4. Điểm mấu chốt

| Thao tác | Vai trò |
|----------|---------|
| `heap.push(num)` | Đưa phần tử mới vào heap |
| `if len(heap) > k: heap.pop()` | Nếu heap vượt quá `k`, loại phần tử **nhỏ nhất** (đỉnh min-heap) |
| `heap[0]` | Đỉnh heap = phần tử nhỏ nhất trong `k` phần tử lớn nhất = **lớn thứ k** |

> **Tại sao loại phần tử nhỏ nhất?** Vì ta muốn giữ lại `k` phần tử **lớn nhất**. Phần tử nhỏ nhất trong heap là "kẻ yếu nhất" trong nhóm `k` — nếu có phần tử mới lớn hơn, nó phải bị loại.

---

## 3. Minh họa từng bước

`nums = [3, 2, 1, 5, 6, 4]`, `k = 2`

| Bước | `num` | Hành động | Heap (sau hành động) | Ghi chú |
|------|-------|-----------|----------------------|---------|
| 1 | 3 | push 3 | `[3]` | len = 1 ≤ k |
| 2 | 2 | push 2 | `[2, 3]` | len = 2 ≤ k |
| 3 | 1 | push 1 → len=3 > k → pop | `[2, 3]` | Loại 1 (nhỏ nhất) |
| 4 | 5 | push 5 → len=3 > k → pop | `[3, 5]` | Loại 2 (nhỏ nhất) |
| 5 | 6 | push 6 → len=3 > k → pop | `[5, 6]` | Loại 3 (nhỏ nhất) |
| 6 | 4 | push 4 → len=3 > k → pop | `[5, 6]` | Loại 4 (nhỏ nhất) |

**Kết quả:** `heap[0] = 5` = phần tử lớn thứ 2. ✅

**Nhận xét:**
- Sau mỗi bước, heap **luôn** chứa `k` phần tử lớn nhất trong đoạn `nums[0..i]` đã duyệt.
- Khi gặp phần tử mới, nếu nó **lớn hơn** phần tử nhỏ nhất trong heap → nó sẽ thay thế phần tử đó.
- Nếu nó **nhỏ hơn hoặc bằng** → bị đẩy vào rồi lập tức bị pop ra (không ảnh hưởng heap).

---

## 4. Cài đặt Python

### 4.1. Cài đặt cơ bản (dùng `heapq`)

```python
import heapq

def find_kth_largest(nums, k):
    """Tìm phần tử lớn thứ k trong mảng."""
    heap = []                            # min-heap

    for num in nums:
        heapq.heappush(heap, num)        # push
        if len(heap) > k:
            heapq.heappop(heap)          # pop phần tử nhỏ nhất

    return heap[0]                       # đỉnh heap = đáp án
```

**Chạy thử:**

```python
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))    # 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
```

### 4.2. Cài đặt tối ưu (dùng `heapreplace`)

Khi `len(heap) == k`, nếu `num > heap[0]` thì thay thế trực tiếp bằng `heapreplace` — nhanh hơn `push` + `pop` riêng.

```python
import heapq

def find_kth_largest_optimized(nums, k):
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)    # chưa đủ k → push
        elif num > heap[0]:
            heapq.heapreplace(heap, num) # num lớn hơn đỉnh → thay thế
        # nếu num <= heap[0]: bỏ qua, không làm gì

    return heap[0]
```

**So sánh:**

| Cách | Thao tác mỗi phần tử | Số thao tác heap |
|------|----------------------|------------------|
| Cơ bản | push + (pop nếu > k) | ~2n |
| Tối ưu | push (nếu < k) hoặc heapreplace (nếu > đỉnh) hoặc bỏ qua | ~n |

### 4.3. Cài đặt bằng `nlargest` (Pythonic nhất)

```python
import heapq

def find_kth_largest_oneliner(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

- `heapq.nlargest(k, nums)` trả về `k` phần tử lớn nhất, **đã sắp xếp giảm dần**.
- `[-1]` lấy phần tử cuối = phần tử nhỏ nhất trong `k` phần tử lớn nhất = **lớn thứ k**.

**Nhưng:** cách này có độ phức tạp `O(n log k)` **và** sắp xếp `k` phần tử (`O(k log k)`) → chậm hơn code tay một chút. Dùng khi cần code ngắn gọn.

### 4.4. Cài đặt bằng Max-Heap (cách "ngược")

Python không có max-heap sẵn, nhưng có thể **đảo dấu** để giả lập:

```python
import heapq

def find_kth_largest_maxheap(nums, k):
    # Đảo dấu để min-heap hoạt động như max-heap
    heap = [-num for num in nums]
    heapq.heapify(heap)

    # Pop k-1 lần → phần tử lớn nhất bị loại dần
    for _ in range(k - 1):
        heapq.heappop(heap)

    return -heap[0]
```

**Nhưng cách này tệ hơn:** phải heapify **toàn bộ** mảng (`O(n)`), rồi pop `k-1` lần (`O(k log n)`). Nếu `k` lớn → chậm hơn nhiều so với Min-Heap k phần tử.

---

## 5. Vì sao dùng Min-Heap mà không dùng Max-Heap?

Đây là câu hỏi **rất hay gặp** — nhiều người thắc mắc: "Tìm lớn thứ k sao lại dùng min-heap?"

### 5.1. Lý do cốt lõi

> **Ta chỉ cần giữ `k` phần tử lớn nhất, và cần biết phần tử NÀO trong đó là nhỏ nhất để loại khi có phần tử mới lớn hơn.**
> → Cần truy cập nhanh **phần tử nhỏ nhất trong nhóm `k` phần tử lớn nhất** → **Min-Heap**.

### 5.2. So sánh trực quan

**Dùng Min-Heap k phần tử:**

```
Duyệt mảng → giữ k phần tử lớn nhất → đỉnh heap = phần tử nhỏ nhất trong k phần tử đó = lớn thứ k
```

- Heap kích thước **k** (nhỏ) → bộ nhớ `O(k)`
- Mỗi phần tử: `O(log k)`
- Tổng: `O(n log k)`

**Dùng Max-Heap toàn bộ:**

```
Đưa cả mảng vào max-heap → pop k-1 lần → đỉnh còn lại = lớn thứ k
```

- Heap kích thước **n** (lớn) → bộ nhớ `O(n)`
- Heapify: `O(n)`, pop k-1 lần: `O(k log n)`
- Tổng: `O(n + k log n)`
- Khi `k` lớn (gần `n`) → `O(n log n)` → chậm hơn Min-Heap k phần tử

### 5.3. Bảng so sánh

| Tiêu chí | Min-Heap k phần tử | Max-Heap toàn bộ |
|----------|--------------------|-------------------|
| Kích thước heap | `k` | `n` |
| Bộ nhớ | `O(k)` | `O(n)` |
| Thời gian | `O(n log k)` | `O(n + k log n)` |
| Khi `k` nhỏ | ✅ Rất nhanh | ⚠️ Chậm hơn |
| Khi `k ≈ n` | `O(n log n)` | `O(n log n)` — tương đương |
| Dùng cho stream | ✅ Có (không cần lưu toàn bộ) | ❌ Không |
| Code Python | Đơn giản | Phải đảo dấu |

### 5.4. Kết luận

> **Min-Heap k phần tử** là lựa chọn tối ưu vì:
> 1. Bộ nhớ chỉ `O(k)` — quan trọng khi `k` nhỏ, dữ liệu lớn
> 2. Thời gian `O(n log k)` — nhanh hơn khi `k` nhỏ
> 3. **Xử lý được stream** — không cần biết toàn bộ mảng trước
> 4. Code Python đơn giản (không cần đảo dấu)

---

## 6. So sánh các cách giải

### 6.1. Code từng cách

```python
# Cách 1: Sort
def kth_largest_sort(nums, k):
    return sorted(nums, reverse=True)[k - 1]
    # hoặc sorted(nums)[-k]

# Cách 2: Min-Heap k phần tử
import heapq
def kth_largest_heap(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# Cách 3: Quickselect (trung bình O(n))
import random
def kth_largest_quickselect(nums, k):
    target = len(nums) - k      # đổi sang "thứ target theo tăng dần"

    def quickselect(left, right):
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        store = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]

        if store == target:   return nums[store]
        elif store < target:  return quickselect(store + 1, right)
        else:                 return quickselect(left, store - 1)

    return quickselect(0, len(nums) - 1)
```

### 6.2. Bảng so sánh

| Cách | Thời gian | Bộ nhớ | Stream? | Ghi chú |
|------|-----------|--------|---------|---------|
| **Sort** | `O(n log n)` | `O(n)` | ❌ | Đơn giản nhất, nhưng chậm |
| **Min-Heap k** | `O(n log k)` | `O(k)` | ✅ | **Cân bằng nhất** |
| **Quickselect** | TB `O(n)`, xấu `O(n²)` | `O(1)` | ❌ | Nhanh nhất trung bình, nhưng worst-case tệ |

### 6.3. Khi nào dùng cách nào?

| Tình huống | Nên dùng |
|------------|----------|
| `k` nhỏ, `n` lớn | **Min-Heap** |
| Dữ liệu stream (không lưu được toàn bộ) | **Min-Heap** |
| Cần code ngắn gọn, `n` nhỏ | **Sort** |
| Cần nhanh nhất trung bình, không sợ worst-case | **Quickselect** |
| Đề phỏng vấn hỏi "tối ưu" | **Min-Heap** hoặc **Quickselect** |

---

## 7. Độ phức tạp

### 7.1. Min-Heap k phần tử

- **Thời gian:** `O(n log k)`
  - Mỗi phần tử: `push` `O(log k)`, có thể thêm `pop` `O(log k)` → tổng `O(log k)` mỗi phần tử
  - `n` phần tử → `O(n log k)`
- **Bộ nhớ:** `O(k)` — heap chỉ chứa tối đa `k` phần tử

### 7.2. So sánh với `k` khác nhau

| `k` | `log k` | Tổng `O(n log k)` | So với sort `O(n log n)` |
|-----|---------|-------------------|--------------------------|
| 1 | 0 | `O(n)` | Nhanh hơn nhiều |
| 10 | ~3.3 | `O(3.3n)` | Nhanh hơn |
| 100 | ~6.6 | `O(6.6n)` | Nhanh hơn |
| `n/2` | ~`log n - 1` | ~`O(n log n)` | Tương đương |
| `n` | `log n` | `O(n log n)` | Tương đương |

→ **`k` càng nhỏ, Min-Heap càng có lợi.**

---

## 8. Biến thể: Kth Smallest

### 8.1. Ý tưởng

Tương tự Kth Largest nhưng **đảo ngược**: dùng **Max-Heap k phần tử nhỏ nhất**.

> Duy trì Max-Heap chứa `k` phần tử **nhỏ nhất**. Đỉnh heap (phần tử lớn nhất trong nhóm nhỏ nhất) = **nhỏ thứ k**.

### 8.2. Cài đặt

Python không có max-heap → **đảo dấu**:

```python
import heapq

def find_kth_smallest(nums, k):
    """Tìm phần tử nhỏ thứ k."""
    heap = []                              # max-heap giả lập bằng đảo dấu

    for num in nums:
        heapq.heappush(heap, -num)         # push -num
        if len(heap) > k:
            heapq.heappop(heap)            # pop phần tử lớn nhất (đảo dấu = -num nhỏ nhất)

    return -heap[0]                        # đảo dấu lại
```

**Chạy thử:**

```python
print(find_kth_smallest([3, 2, 1, 5, 6, 4], 2))   # 2
# Sắp tăng dần: [1, 2, 3, 4, 5, 6] → nhỏ thứ 2 là 2
```

### 8.3. Vì sao đảo dấu hoạt động?

- `heapq` chỉ có **min-heap**.
- Muốn có **max-heap** → lưu **số đối** (`-num`).
- Phần tử lớn nhất (theo giá trị gốc) = phần tử nhỏ nhất (theo `-num`) → nằm ở đỉnh.
- Khi lấy ra: `-heap[0]` để trả về giá trị gốc.

---

## 9. Biến thể: K phần tử lớn nhất

### 9.1. Đề bài (LeetCode 347 — Top K Frequent Elements, hoặc biến thể)

Trả về **`k` phần tử lớn nhất** (không chỉ một phần tử).

### 9.2. Cài đặt

```python
import heapq

def top_k_largest(nums, k):
    """Trả về k phần tử lớn nhất (không sắp xếp)."""
    return heapq.nlargest(k, nums)


def top_k_largest_sorted(nums, k):
    """Trả về k phần tử lớn nhất, đã sắp xếp giảm dần."""
    return sorted(heapq.nlargest(k, nums), reverse=True)
```

**Chạy thử:**

```python
print(top_k_largest([3, 2, 1, 5, 6, 4], 3))    # [6, 5, 4]
```

### 9.3. Tự cài bằng heap

```python
import heapq

def top_k_largest_manual(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap          # heap chứa k phần tử lớn nhất (không sort)
```

### 9.4. Liên hệ với Kth Largest

> **Kth Largest = phần tử nhỏ nhất trong Top K Largest.**
>
> Nếu đã có `top_k_largest(nums, k)` → `min(top_k_largest(...)) = kth_largest(nums, k)`.
>
> Và vì heap là min-heap → `heap[0]` chính là phần tử đó. Đó là lý do code Kth Largest chỉ cần `return heap[0]`.

---

## 10. Lỗi thường gặp

### 10.1. Nhầm "lớn thứ k" với "nhỏ thứ k"

```python
# ❌ Sai — tưởng k tính từ nhỏ
nums = [3, 2, 1, 5, 6, 4]
k = 2
# Nếu hiểu "nhỏ thứ 2" → 2 (SAI)
# Đúng phải là "lớn thứ 2" → 5
```

**Cách nhớ:** `k = 1` → phần tử **lớn nhất**; `k = n` → phần tử **nhỏ nhất**.

### 10.2. Dùng Max-Heap cho Kth Largest

```python
# ❌ Không sai về kết quả, nhưng chậm và tốn bộ nhớ
def kth_largest_wrong(nums, k):
    heap = [-num for num in nums]
    heapq.heapify(heap)
    for _ in range(k - 1):
        heapq.heappop(heap)
    return -heap[0]
# Đúng kết quả, nhưng O(n + k log n) thay vì O(n log k)
```

### 10.3. Quên kiểm tra `k` hợp lệ

```python
# ❌ Không kiểm tra
def find_kth_largest(nums, k):
    ...
# Nếu k <= 0 hoặc k > len(nums) → lỗi hoặc kết quả sai

# ✅ Kiểm tra
def find_kth_largest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("k phải trong khoảng [1, len(nums)]")
    ...
```

### 10.4. Nhầm `heappush` và `heapify`

```python
# ❌ Sai — heapify không thêm phần tử mới
heap = []
for num in nums:
    heapq.heapify(heap)       # vô nghĩa, heap đang rỗng
    heap.append(num)

# ✅ Đúng
for num in nums:
    heapq.heappush(heap, num)
```

### 10.5. Dùng `heappop` sai chỗ

```python
# ❌ Sai — pop khi heap chưa vượt k
for num in nums:
    heapq.heappush(heap, num)
    heapq.heappop(heap)       # luôn pop → heap chỉ còn 1 phần tử

# ✅ Đúng
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
```

### 10.6. Nhầm `heapreplace` với `heappushpop`

| Hàm | Hành vi | Khi nào dùng |
|-----|---------|--------------|
| `heapq.heapreplace(heap, x)` | Pop đỉnh cũ → push `x` (1 thao tác) | Khi biết chắc `x > heap[0]` |
| `heapq.heappushpop(heap, x)` | Push `x` → pop đỉnh (1 thao tác) | Khi không chắc `x` so với đỉnh |

**Lưu ý:** `heappushpop` trả về phần tử bị pop — có thể là `x` nếu `x` nhỏ hơn đỉnh. `heapreplace` luôn pop đỉnh cũ.

---

## 11. Kết luận

> **Kth Largest = duy trì Min-Heap kích thước `k` chứa `k` phần tử lớn nhất; đỉnh heap (`heap[0]`) là phần tử lớn thứ `k`.**

**Tóm tắt các ý chính:**

| Ý | Nội dung |
|---|----------|
| **Ý tưởng** | Min-Heap k phần tử — giữ `k` phần tử lớn nhất, đỉnh = nhỏ nhất trong nhóm = lớn thứ `k` |
| **Thuật toán** | Với mỗi `num`: push; nếu `len > k` thì pop |
| **Tối ưu** | Dùng `heapreplace` khi `num > heap[0]` |
| **Python** | `heapq.heappush`, `heapq.heappop`, `heapq.heapreplace`, `heapq.nlargest` |
| **Độ phức tạp** | `O(n log k)` thời gian, `O(k)` bộ nhớ |
| **Vì sao Min-Heap?** | Cần truy cập nhanh **phần tử nhỏ nhất trong nhóm `k` phần tử lớn nhất** |
| **Kth Smallest** | Đảo ngược: Max-Heap (đảo dấu) k phần tử nhỏ nhất |
| **Top K Largest** | Cùng heap, trả về cả `heap` thay vì `heap[0]` |

**Câu chốt để nhớ:**

```
Kth Largest  → Min-Heap k phần tử  → heap[0]
Kth Smallest → Max-Heap k phần tử  → -heap[0]
Top K Largest → Min-Heap k phần tử → return heap (cả list)
```

**Code "one-liner" Pythonic nhất:**

```python
import heapq
def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

**Code "phỏng vấn" (tự cài, thể hiện hiểu thuật toán):**

```python
import heapq
def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
```
