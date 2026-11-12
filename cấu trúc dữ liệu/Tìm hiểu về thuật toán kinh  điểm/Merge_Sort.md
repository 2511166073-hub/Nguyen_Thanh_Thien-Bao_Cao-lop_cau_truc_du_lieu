
# Merge Sort — Giải Thích Chi Tiết Từ Gốc Đến Ứng Dụng

> Tài liệu hoàn chỉnh về **Merge Sort**: ý tưởng, chứng minh độ phức tạp, code 3 phiên bản, phân tích stable, so sánh thuật toán, ứng dụng thực tế, bottom-up, bẫy, câu hỏi tự kiểm có đáp án, và bảng tóm tắt.

---

## Mục lục

1. [Ý tưởng cốt lõi](#1-ý-tưởng-cốt-lõi)
2. [Ví dụ chạy tay chi tiết](#2-ví-dụ-chạy-tay-chi-tiết)
3. [Code Python (3 phiên bản)](#3-code-python-3-phiên-bản)
4. [Độ phức tạp — chứng minh đầy đủ](#4-độ-phức-tạp--chứng-minh-đầy-đủ)
5. [Tính chất Stable — vì sao và ở đâu](#5-tính-chất-stable--vì-sao-và-ở-đâu)
6. [So sánh với Quick Sort / Heap Sort / Timsort](#6-so-sánh-với-quick-sort--heap-sort--timsort)
7. [Ba ứng dụng đáng biết](#7-ba-ứng-dụng-đáng-biết)
8. [Bottom-up Merge Sort (khử đệ quy)](#8-bottom-up-merge-sort-khử-đệ-quy)
9. [Bẫy thường gặp khi code / khi thi](#9-bẫy-thường-gặp-khi-code--khi-thi)
10. [Câu hỏi tự kiểm + đáp án](#10-câu-hỏi-tự-kiểm--đáp-án)
11. [Tóm tắt một trang](#11-tóm-tắt-một-trang)

---

## 1. Ý tưởng cốt lõi

### 1.1. Quan sát then chốt

Bài toán gốc — **sắp xếp một dãy lộn xộn** — được coi là "khó".

Nhưng có một bài toán con **rất dễ**:

> **Gộp (merge) hai dãy ĐÃ sắp xếp thành một dãy sắp xếp chỉ tốn `O(n)`.**

Vì sao dễ? Chỉ cần **2 con trỏ** chạy song song từ đầu mỗi dãy, mỗi bước so sánh 2 phần tử ở đầu con trỏ, lấy phần tử nhỏ hơn, rồi nhích con trỏ đó lên. Mỗi phần tử được "chạm" đúng 1 lần → tuyến tính.

### 1.2. Đảo ngược vấn đề

Merge Sort dựa trên mẹo tư duy:

> Thay vì cố sắp xếp cả dãy khó, hãy **chia nhỏ đến mức không thể chia** — mỗi phần còn 1 phần tử (1 phần tử đương nhiên "đã sắp xếp") — rồi **gộp dần lên**.

Đây chính là chiến lược **Divide & Conquer (chia để trị)**.


### 1.3. Ba bước chuẩn của Divide & Conquer

        ┌─────────────┐
        │   DIVIDE    │  Chia đôi dãy
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │  CONQUER    │  Đệ quy sắp xếp từng nửa
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │  COMBINE    │  Merge 2 nửa đã sắp xếp
        └─────────────┘

**Điểm hay:** toàn bộ "công việc thật" bị đẩy xuống bước **merge**, và merge rất rẻ.


### 1.4. Trực giác cây đệ quy
```text
                    [n phần tử]           ← tầng 0: 1 bài toán size n
                   /            \
            [n/2]                [n/2]     ← tầng 1: 2 bài toán size n/2
           /    \                /    \
        [n/4]  [n/4]         [n/4]   [n/4]  ← tầng 2: 4 bài toán size n/4
          ...    ...           ...     ...
         [1] [1] [1] [1] ... [1] [1] [1] [1]  ← tầng log₂n: n bài toán size 1
```

- **Chiều sâu cây:** `log₂ n` (vì mỗi tầng chia đôi).
- **Tổng công việc mỗi tầng:** `O(n)` (mỗi phần tử bị chạm 1 lần trong merge).
- **Tổng cộng:** `O(n log n)`.



## 2. Ví dụ chạy tay chi tiết

Cho `a = [38, 27, 43, 3, 9, 82, 10, 25]`

### 2.1. Pha chia (đi xuống)

```
                [38,27,43,3,9,82,10,25]
              /                          \
      [38,27,43,3]                    [9,82,10,25]
       /       \                       /        \
   [38,27]   [43,3]                [9,82]     [10,25]
    /   \     /   \                 /  \       /   \
 [38] [27] [43]  [3]             [9] [82]  [10]  [25]
```

Dừng khi mỗi đoạn còn **1 phần tử** — đó là base case.

### 2.2. Pha gộp (đi lên)

```text
 [27,38]   [3,43]               [9,82]     [10,25]
      \      /                       \       /
   [3,27,38,43]                    [9,10,25,82]
              \                      /
        [3,9,10,25,27,38,43,82]
```


### 2.3. Chi tiết bước merge cuối — `L = [3,27,38,43]`, `R = [9,10,25,82]`

| Bước | i (L) | j (R) | So sánh | Lấy | Kết quả tích lũy |
|---|---|---|---|---|---|
| 1 | 3 | 9 | 3 ≤ 9 | 3 (L) | `[3]` |
| 2 | 27 | 9 | 27 > 9 | 9 (R) | `[3,9]` |
| 3 | 27 | 10 | 27 > 10 | 10 (R) | `[3,9,10]` |
| 4 | 27 | 25 | 27 > 25 | 25 (R) | `[3,9,10,25]` |
| 5 | 27 | 82 | 27 ≤ 82 | 27 (L) | `[3,9,10,25,27]` |
| 6 | 38 | 82 | 38 ≤ 82 | 38 (L) | `[...,38]` |
| 7 | 43 | 82 | 43 ≤ 82 | 43 (L) | `[...,43]` |
| 8 | hết | 82 | — | copy 82 | `[3,9,10,25,27,38,43,82]` |

**Nhận xét quan trọng:**
- Mỗi phần tử của `L` và `R` bị "chạm" **đúng 1 lần** → merge tốn `O(n)`.
- Khi một nửa cạn, **copy thẳng** phần còn lại của nửa kia (bước 8).
- Phép so sánh dùng `≤` (không phải `<`) để giữ **stability** — xem mục 5.

### 2.4. Tổng số thao tác

Với `n = 8`:
- Tầng merge 1: 4 cặp độ dài 2 → 4×1 so sánh = 4
- Tầng merge 2: 2 cặp độ dài 4 → 2×~3 = 6
- Tầng merge 3: 1 cặp độ dài 8 → ~7
- **Tổng ≈ 17 so sánh** (đúng công thức `n log₂ n − n + 1 = 8×3 − 8 + 1 = 17` ✅)

---

## 3. Code Python (3 phiên bản)

### 3.1. Dùng slicing

```python
def merge(left: list, right: list) -> list:
    """Gộp 2 dãy đã sắp xếp thành 1 dãy sắp xếp."""
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:      # <= để GIỮ tính stable
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])             # một trong hai sẽ rỗng
    out.extend(right[j:])
    return out


def merge_sort(a: list) -> list:
    if len(a) <= 1:                  # base case
        return a[:]
    mid = len(a) // 2
    left  = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)
```

**Ưu:** đọc hiểu trong 10 giây, đúng bản chất thuật toán.
**Nhược:** `a[:mid]` và `a[mid:]` **sao chép mảng ở mỗi lần gọi** → tổng bộ nhớ phụ thực tế lớn hơn `O(n)` (do nhiều bản sao cùng tồn tại trên các nhánh đệ quy).
→ **Chỉ dùng để học**, đừng dùng cho dữ liệu lớn.

### 3.2. Bản dùng 1 buffer phụ duy nhất 

```python
def merge_sort(a: list) -> list:
    """Sắp xếp tại chỗ (in-place) trên a, dùng mảng phụ O(n)."""
    aux = [None] * len(a)
    _sort(a, aux, 0, len(a) - 1)
    return a


def _sort(a, aux, lo, hi):
    if lo >= hi:                     # 0 hoặc 1 phần tử → đã sắp xếp
        return
    mid = (lo + hi) // 2
    _sort(a, aux, lo, mid)
    _sort(a, aux, mid + 1, hi)
    # Tối ưu: nếu 2 nửa đã nối đúng thứ tự → khỏi merge
    if a[mid] <= a[mid + 1]:
        return
    _merge(a, aux, lo, mid, hi)


def _merge(a, aux, lo, mid, hi):
    aux[lo:hi + 1] = a[lo:hi + 1]    # copy 1 lần ra buffer
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:                  # nửa trái cạn
            a[k] = aux[j]; j += 1
        elif j > hi:                 # nửa phải cạn
            a[k] = aux[i]; i += 1
        elif aux[j] < aux[i]:        # < (không phải <=) để giữ stable
            a[k] = aux[j]; j += 1
        else:
            a[k] = aux[i]; i += 1
```

**Ưu:**
- **1 mảng `aux` dùng chung** cho toàn bộ đệ quy → bộ nhớ phụ đúng `O(n)`.
- Tối ưu `a[mid] <= a[mid+1]` bỏ qua merge khi dữ liệu gần sorted.
- Nhanh hơn bản slicing khoảng 2–3×.

**Nhược:** code khó đọc hơn.

### 3.3. Bản hybrid với Insertion Sort cho đoạn nhỏ

Trong thực tế, khi đoạn còn rất nhỏ (≤ 16–32 phần tử), **Insertion Sort nhanh hơn Merge Sort** vì ít overhead đệ quy. Timsort cũng dùng mẹo này.

```python
INSERTION_THRESHOLD = 16

def _sort_hybrid(a, aux, lo, hi):
    if hi - lo + 1 <= INSERTION_THRESHOLD:
        _insertion_sort(a, lo, hi)
        return
    mid = (lo + hi) // 2
    _sort_hybrid(a, aux, lo, mid)
    _sort_hybrid(a, aux, mid + 1, hi)
    if a[mid] <= a[mid + 1]:
        return
    _merge(a, aux, lo, mid, hi)


def _insertion_sort(a, lo, hi):
    for i in range(lo + 1, hi + 1):
        key = a[i]
        j = i - 1
        while j >= lo and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
```

---

## 4. Độ phức tạp — chứng minh đầy đủ

### 4.1. Công thức truy hồi

```
T(n) = 2·T(n/2) + Θ(n),   với T(1) = Θ(1)
       └───┬───┘   └───┬───┘
        2 nửa      chi phí merge
```

### 4.2. Chứng minh bằng Master Theorem

Dạng chuẩn: `T(n) = a·T(n/b) + f(n)` với `a = 2`, `b = 2`, `f(n) = Θ(n)`.

- `n^{log_b a} = n^{log₂ 2} = n¹ = n`.
- So sánh `f(n) = Θ(n)` với `n^{log_b a} = Θ(n)` → **hai vế cùng bậc** → rơi vào **case 2**.
- Kết luận: `T(n) = Θ(n^{log_b a} · log n) = Θ(n log n)`.

### 4.3. Chứng minh bằng cây đệ quy (trực giác)

| Tầng | Số bài toán | Size mỗi bài | Tổng công việc |
|---|---|---|---|
| 0 | 1 | n | `O(n)` |
| 1 | 2 | n/2 | `O(n)` |
| 2 | 4 | n/4 | `O(n)` |
| … | … | … | `O(n)` |
| log₂ n | n | 1 | `O(n)` |

Cộng theo tầng: `log₂ n` tầng × `O(n)`/tầng = **`O(n log n)`**.

### 4.4. Vì sao **mọi trường hợp** đều `n log n`?

Vì **cây đệ quy luôn cân bằng hoàn hảo** — luôn chia đôi ở giữa `mid = n/2`, bất kể dữ liệu đầu vào là gì. Không có trường hợp "may mắn" (nhanh hơn) hay "xui xẻo" (chậm hơn).

Đây là điểm **khác biệt cốt lõi** với Quick Sort (worst case `O(n²)` khi pivot xấu).

### 4.5. Bảng tổng hợp

| Tiêu chí | Giá trị |
|---|---|
| Time best | `Θ(n log n)` |
| Time average | `Θ(n log n)` |
| Time worst | `Θ(n log n)` |
| Space (array) | `O(n)` mảng phụ + `O(log n)` stack |
| Stable | Có (nếu `<=` đúng chỗ) |
| In-place |  Không |
| Số so sánh worst-case | `≈ n·log₂ n − n + 1` |
| Adaptive | Bản gốc: **không**. Timsort: **có** |

### 4.6. Cảm nhận độ lớn

| `n` | `n log₂ n` | `n²` | Tỷ lệ |
|---|---|---|---|
| 10³ | ~10⁴ | 10⁶ | 100× |
| 10⁶ | ~2·10⁷ | 10¹² | 50.000× |
| 10⁹ | ~3·10¹⁰ | 10¹⁸ | 33 triệu × |

Với `n = 10⁶`, độ sâu đệ quy chỉ `log₂(10⁶) ≈ 20` → **không lo `RecursionError`**.

---

## 5. Tính chất Stable — vì sao và ở đâu

### 5.1. Định nghĩa

**Stable sort** = khi hai phần tử **bằng nhau** (theo khóa so sánh), thứ tự **xuất hiện ban đầu** của chúng được giữ nguyên trong kết quả.

Ví dụ: sort theo `(tuổi)` danh sách `[("An", 20), ("Bình", 20), ("Cường", 18)]`:
- Stable → `[("Cường", 18), ("An", 20), ("Bình", 20)]` (An trước Bình vẫn giữ).
- Unstable → có thể ra `[("Cường", 18), ("Bình", 20), ("An", 20)]`.

### 5.2. Dòng code quyết định

**Bản 3.1:**
```python
if left[i] <= right[j]:      # <= chứ không phải <
    out.append(left[i]); i += 1
else:
    out.append(right[j]); j += 1
```
- Khi `left[i] == right[j]`, `<=` **buộc lấy phần tử bên trái trước** → giữ nguyên thứ tự xuất hiện ban đầu (phần tử bên trái đứng trước ban đầu).

**Bản 3.2:**
```python
elif aux[j] < aux[i]:        # < chứ không phải <=
    a[k] = aux[j]; j += 1
else:
    a[k] = aux[i]; i += 1
```
- Khi bằng nhau, điều kiện `<` **sai** → rơi vào `else` → lấy bên trái → **stable**.

### 5.3. Nếu đổi dấu thì sao?

Đổi `<=` thành `<` ở bản 3.1 → khi bằng nhau lấy bên phải trước → **phá vỡ stable** (đây là bẫy thi kinh điển).

---

## 6. So sánh với Quick Sort / Heap Sort / Timsort

| | Merge Sort | Quick Sort | Heap Sort | Timsort |
|---|---|---|---|---|
| Worst case | `n log n` ✅ | `n²` ❌ | `n log n` | `n log n` |
| Average | `n log n` | `n log n` | `n log n` | `n log n` |
| Thực tế (cache) | trung bình | **nhanh nhất** | chậm nhất | **nhanh nhất trên dữ liệu thực** |
| Bộ nhớ phụ | `O(n)` | `O(log n)` | `O(1)` | `O(n)` |
| Stable | ✅ | ❌ | ❌ | ✅ |
| In-place | ❌ | ✅ (gần) | ✅ | ❌ |
| Sort linked list | ✅ tốt nhất | kém | không dùng | — |
| External sort (> RAM) | ✅ | ❌ | ❌ | — |
| Adaptive | ❌ (bản gốc) | ❌ | ❌ | ✅ |

### 6.1. Khi nào dùng cái nào?

- **Dữ liệu nhỏ (< 32):** Insertion Sort.
- **Cần stable, không quan tâm bộ nhớ:** Merge Sort / Timsort.
- **Cần nhanh, không cần stable:** Quick Sort (với 3-way partition).
- **Cần `O(1)` memory tuyệt đối:** Heap Sort.
- **Dữ liệu thực thế:** Timsort (`sorted()` của Python).
- **Dữ liệu lớn hơn RAM:** External Merge Sort.

### 6.2. Vì sao Python dùng Timsort?

`sorted()` / `list.sort()` của Python dùng **Timsort** = **Merge Sort + Insertion Sort**, vì:
1. **Stable** — quan trọng với sort nhiều khóa (`sort(key=...)` chạy nhiều lần).
2. **`O(n log n)` worst case** — không bao giờ bị `O(n²)` như Quick Sort thuần.
3. **Adaptive** — phát hiện "run" (đoạn đã sorted) có sẵn, dùng Insertion Sort cho run ngắn → nhanh hơn Merge Sort thuần trên dữ liệu thực 1.5–3×.
4. **Galloping mode** — khi merge 1 dãy dài với 1 phần tử nhỏ, "nhảy cóc" bằng binary search thay vì so sánh tuần tự.

**Kết luận thực dụng:** đi làm → **cứ dùng `sorted()`**. Học Merge Sort là để hiểu *bên trong*, và để xử lý các bài toán đặc thù bên dưới.

---

## 7. Ba ứng dụng đáng biết

### 7.1. Đếm nghịch thế (inversion count)

**Bài toán:** đếm số cặp `(i, j)` với `i < j` và `a[i] > a[j]`.
Brute force: `O(n²)`. Dùng Merge Sort: `O(n log n)`.

**Mẹo:** trong lúc merge, mỗi khi lấy phần tử từ nửa **phải**, nó "vượt qua" toàn bộ phần còn lại của nửa trái → cộng thêm `len(L) − i` nghịch thế.

```python
def count_inversions(a: list) -> int:
    def sort_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        L, x = sort_count(a[:mid])
        R, y = sort_count(a[mid:])
        merged, z, i, j = [], 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                merged.append(L[i]); i += 1
            else:
                merged.append(R[j]); j += 1
                z += len(L) - i          # <-- dòng thần thánh
        merged += L[i:]; merged += R[j:]
        return merged, x + y + z
    return sort_count(a)[1]

print(count_inversions([2, 4, 1, 3, 5]))   # 3
```

**Liên quan:** số nghịch thế = "khoảng cách" tới dãy tăng dần → là nền tảng tính **Kendall's tau** trong thống kê, và **rank correlation** trong ML.

### 7.2. External Merge Sort — dữ liệu lớn hơn RAM

**Bài toán:** file CSV 100 GB, RAM 16 GB → không thể `load` toàn bộ.

**Ý tưởng:** chia thành các "chunk" vừa RAM, sort từng chunk, ghi ra file tạm, cuối cùng **k-way merge** các file tạm.

```python
import heapq, os, tempfile

def external_sort(src, dst, key, chunk_size=1_000_000):
    files = []
    with open(src) as f:
        while True:
            lines = [f.readline() for _ in range(chunk_size)]
            lines = [l for l in lines if l]
            if not lines:
                break
            lines.sort(key=key)                     # sort chunk trong RAM
            tmp = tempfile.NamedTemporaryFile('w+', delete=False)
            tmp.writelines(lines); tmp.flush()
            files.append(tmp)
    with open(dst, 'w') as out:                     # k-way merge
        out.writelines(heapq.merge(*files, key=key))
    for t in files:
        t.close(); os.unlink(t.name)
```

`heapq.merge` = **merge k chiều** — cùng nguyên lý 2 con trỏ, nhưng dùng heap `k` con trỏ → `O(n log k)`.

**Rất sát với công việc GIS / remote sensing:** point cloud, CSV hàng chục GB, pixel time series.

### 7.3. Merge Sort trên linked list

**Vì sao merge sort hợp linked list?**

| | Array | Linked list |
|---|---|---|
| Random access | `O(1)` | `O(n)` ← Quick Sort cần cái này |
| Chèn / xóa | `O(n)` | `O(1)` ← Merge Sort tận dụng |
| Merge 2 list | `O(n)` + `O(n)` memory | `O(n)` + `O(1)` memory ✅ |

→ Merge Sort trên linked list: `O(n log n)` time, **`O(1)` extra space** (nếu viết bottom-up).
Đây là lý do **nhiều thư viện** (kể cả Linux kernel, Java LinkedList) sort list bằng merge sort.

**Code mẫu:**

```python
class Node:
    def __init__(self, val, nxt=None):
        self.val, self.next = val, nxt

def merge_lists(a, b):
    dummy = Node(0)
    tail = dummy
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next

def merge_sort_list(head):
    if not head or not head.next:
        return head
    # tìm mid bằng slow/fast pointer
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    mid = slow.next
    slow.next = None
    return merge_lists(merge_sort_list(head), merge_sort_list(mid))
```

---

## 8. Bottom-up Merge Sort (khử đệ quy)

### 8.1. Ý tưởng

Không đệ quy chia đôi, mà **gộp từ dưới lên**:
- Ban đầu coi mỗi phần tử là 1 đoạn đã sorted (độ dài 1).
- Gộp các cặp đoạn độ dài `1 → 2`, `2 → 4`, `4 → 8`, …
- Lặp đến khi 1 đoạn độ dài `n`.

### 8.2. Code

```python
def merge_sort_bottom_up(a: list) -> list:
    n = len(a)
    width = 1
    aux = [None] * n
    while width < n:
        for lo in range(0, n, 2 * width):
            mid = min(lo + width - 1, n - 1)
            hi  = min(lo + 2 * width - 1, n - 1)
            if mid < hi:
                _merge(a, aux, lo, mid, hi)
        width *= 2
    return a
```

### 8.3. Ưu / nhược

| Ưu | Nhược |
|---|---|
| Không cần stack đệ quy | Code hơi khó đọc hơn |
| Dễ viết trên linked list | Không tự nhiên với dữ liệu "gần sorted" |
| Không lo `RecursionError` | Không phải bản Timsort dùng |

---

## 9. Bẫy thường gặp khi code / khi thi

| # | Bẫy | Hậu quả |
|---|---|---|
| 1 | Dùng `<` thay `<=` ở nhánh lấy bên trái | **Mất stable** (thi rất hay hỏi) |
| 2 | Quên `extend` phần còn lại sau `while` | Mất phần tử |
| 3 | Base case `len(a) == 0` mà không xử lý `== 1` | Đệ quy vô hạn |
| 4 | Nghĩ Merge Sort là in-place trên array | Sai — tốn `O(n)` phụ |
| 5 | `mid = (lo + hi) / 2` (chia thực) thay `//` (chia nguyên) | `IndexError` |
| 6 | Copy `aux[lo:hi+1]` **bên trong** vòng for | Chậm `O(n²)` |
| 7 | Dùng `+` để nối list trong vòng lặp | Tạo list mới `O(n²)` |
| 8 | Không tối ưu `a[mid] <= a[mid+1]` | Chậm hơn 10–20% trên gần-sorted |

---

## 10. Câu hỏi tự kiểm + đáp án

### Câu 1: Vì sao worst case của Merge Sort luôn `n log n` còn Quick Sort thì không?

**Đáp:** Merge Sort **luôn chia đôi ở giữa** (`mid = n/2`) bất kể dữ liệu → cây đệ quy luôn cân bằng, sâu `log₂ n`. Quick Sort chọn pivot; nếu pivot xấu (min/max) với dữ liệu đã sorted → chia lệch hoàn toàn `(0, n−1)` → cây thành "dây xích" sâu `n` → `O(n²)`.

### Câu 2: Merge Sort có stable không? Chỉ ra chính xác dòng code quyết định.

**Đáp:** Có. Dòng quyết định:
- Bản dễ hiểu: `if left[i] <= right[j]:`
- Bản buffer: `elif aux[j] < aux[i]:`

Khi 2 phần tử **bằng nhau**, `<=` (hoặc `<` ở dạng đảo) buộc lấy **bên trái trước** → giữ nguyên thứ tự xuất hiện ban đầu.

### Câu 3: Với `n = 1024`, có bao nhiêu tầng merge và tối đa bao nhiêu so sánh?

**Đáp:**
- Số tầng: `log₂ 1024 = 10`.
- Số so sánh tối đa: `n·log₂n − n + 1 = 1024×10 − 1024 + 1 = 9217`.

### Câu 4: Vì sao Timsort nhanh hơn Merge Sort thuần trên dữ liệu thực tế?

**Đáp:** Dữ liệu thực thường có **"run"** — các đoạn đã sắp xếp sẵn. Timsort:
1. Phát hiện run.
2. Dùng Insertion Sort cho run ngắn (< 32 hoặc < 64).
3. Merge thông minh với **galloping mode** (dùng binary search khi một dãy lớn hơn nhiều dãy kia).
4. **Adaptive** — chỉ tốn `O(n)` nếu dữ liệu đã sorted.

→ Giảm mạnh số so sánh so với chia-đôi-mù-quáng.

### Câu 5: Viết bottom-up merge sort.

**Đáp:** Xem mục 8.

### Câu 6: Tại sao Merge Sort tốt cho linked list hơn Quick Sort?

**Đáp:** Linked list không có random access — Quick Sort cần truy cập `a[mid]` liên tục → `O(n)` mỗi lần. Merge Sort chỉ cần duyệt tuần tự → tự nhiên hợp với linked list. Ngoài ra merge 2 list chỉ tốn `O(1)` extra space (chỉ đổi con trỏ).

### Câu 7: Merge Sort có phải in-place không?

**Đáp:** **Không** trên array (tốn `O(n)` mảng phụ). Trên **linked list** thì có thể coi là "in-place" theo nghĩa `O(1)` extra space (chỉ đổi con trỏ) nếu viết đúng.

### Câu 8: Khi nào Merge Sort chậm hơn Quick Sort?

**Đáp:** Thực tế (không phải worst-case lý thuyết):
- Merge Sort **không cache-friendly** — truy cập 2 vùng nhớ khác nhau (`left` và `right`) khi merge → nhiều cache miss.
- Quick Sort partition làm việc trên 1 mảng → cache-friendly hơn.
- Trên mảng lớn, Quick Sort trung bình nhanh hơn Merge Sort khoảng **1.5–2×**.

---

## 11. Tóm tắt một trang

```
┌─────────────────────────────────────────────────────────┐
│                    MERGE SORT                           │
├─────────────────────────────────────────────────────────┤
│ Ý tưởng:  Chia đôi → đệ quy → merge 2 con trỏ           │
│ Chiến lược: Divide & Conquer                            │
│                                                         │
│ Độ phức tạp:                                            │
│   • Time:   Θ(n log n) — MỌI trường hợp                 │
│   • Space:  O(n) + O(log n) stack                       │
│                                                         │
│ Tính chất:                                              │
│   • Stable ✅                                           │
│   • In-place ❌ (trên array)                            │
│   • Adaptive ❌ (bản gốc)                               │
│                                                         │
│ Dùng khi:                                               │
│   • Cần stable sort                                     │
│   • Sort linked list                                    │
│   • External sort (> RAM)                               │
│   • Không chấp nhận worst case n²                       │
│                                                         │
│ Ứng dụng:                                               │
│   • Đếm nghịch thế (Kendall's tau)                      │
│   • External sort (GIS, big data)                       │
│   • Sort linked list (Java, Linux kernel)               │
│                                                         │
│ Trong Python: sorted() = Timsort = Merge + Insertion    │
│ → Đi làm: cứ dùng sorted(). Học để hiểu + bài toán đặc. │
└─────────────────────────────────────────────────────────┘
```

---

## Phụ lục: Benchmark so sánh thực tế

```python
import timeit, random
from functools import partial

# Chuẩn bị dữ liệu
for n in [1_000, 10_000, 100_000]:
    data = [random.randint(0, 10**6) for _ in range(n)]
    t_merge = timeit.timeit(partial(merge_sort, data.copy()), number=10) / 10
    t_builtin = timeit.timeit(partial(sorted, data.copy()), number=10) / 10
    print(f"n={n:>7,}  merge={t_merge*1000:8.2f}ms  sorted={t_builtin*1000:8.2f}ms  "
          f"ratio={t_merge/t_builtin:.2f}x")
```

**Kết quả kỳ vọng (máy thường):**

| n | Merge Sort | `sorted()` (Timsort) | Tỷ lệ |
|---|---|---|---|
| 1.000 | ~0.5 ms | ~0.1 ms | ~5× |
| 10.000 | ~6 ms | ~1 ms | ~6× |
| 100.000 | ~80 ms | ~15 ms | ~5× |

→ Timsort nhanh hơn Merge Sort thuần **3–6×** trên dữ liệu ngẫu nhiên, và còn nhanh hơn nữa trên dữ liệu gần-sorted.

---

## Tài liệu tham khảo

- CLRS — *Introduction to Algorithms*, chương 2 (Merge Sort).
- Sedgewick & Wayne — *Algorithms*, chương 2.2 (Mergesort).
- Tim Peters — *Timsort* (Python source `listsort.txt`).
- Knuth — *TAOCP Vol. 3*, mục 5.2.4 (Merge Sort).

---

**Hết.**
```
