# 🎯 Two Sum — Tìm cặp số có tổng bằng target

> Bài toán kinh điển về **tối ưu thuật toán**: từ Brute-force `O(n²)` lên Hash Map `O(n)`.

---

## 📋 Mục lục

- [1. Bài toán](#1-bài-toán)
- [2. Ba cách giải](#2-ba-cách-giải)
- [3. Code Python đầy đủ](#3-code-python-đầy-đủ)
- [4. Phân tích bộ nhớ — điểm quan trọng](#4-phân-tích-bộ-nhớ--điểm-quan-trọng)
- [5. Benchmark thực tế](#5-benchmark-thực-tế)
- [6. Bảng so sánh tổng kết](#6-bảng-so-sánh-tổng-kết)
- [7. Bài tập mở rộng](#7-bài-tập-mở-rộng)
- [8. Bài học rút ra](#8-bài-học-rút-ra)

---

## 1. Bài toán

Cho một mảng số nguyên **chưa sắp xếp** và một số `target`. Tìm **hai phần tử** trong mảng sao cho tổng của chúng bằng `target`.

### Ví dụ

```text
Input:  nums = [8, 7, 2, 5, 3, 1],  target = 10
Output: (8, 2)   vì 8 + 2 = 10
        hoặc (7, 3) vì 7 + 3 = 10

Input:  nums = [5, 2, 6, 8, 1, 9],  target = 12
Output: Pair not found
```

**Lưu ý:**
- Mảng **chưa sắp xếp** — đây là điểm làm bài toán khó.
- Chỉ cần tìm **một cặp** là đủ.
- Hai phần tử phải ở **hai vị trí khác nhau**.

---

## 2. Ba cách giải

### 🐢 Cách 1 — Brute-force (vét cạn)

Thử **mọi cặp** có thể. Với mỗi phần tử `i`, ghép với mọi phần tử `j` phía sau.

**Ưu điểm:** Đơn giản, đúng, `O(1)` bộ nhớ.
**Nhược điểm:** `O(n²)` — chậm kinh khủng với mảng lớn.

### ⚖️ Cách 2 — Sorting + Hai con trỏ

1. Sắp xếp mảng tăng dần.
2. Đặt 2 con trỏ `low` (đầu) và `high` (cuối).
3. So tổng `nums[low] + nums[high]` với target, thu hẹp dần phạm vi.

**Ưu điểm:** `O(n log n)` — khá nhanh.
**Nhược điểm:** Phá thứ tự gốc; trong Python `list.sort()` tốn `O(n)` bộ nhớ (Timsort).

### 🚀 Cách 3 — Hashing (bảng băm)

Vừa duyệt mảng, vừa ghi các số đã gặp vào "sổ" (Hash Map). Với mỗi `num`, kiểm tra `target - num` đã có trong sổ chưa.

**Ưu điểm:** `O(n)` — nhanh nhất.
**Nhược điểm:** Tốn `O(n)` bộ nhớ cho cuốn sổ.

---

## 3. Code Python đầy đủ

```python
# ============================================================
# CÁCH 1: BRUTE-FORCE — O(n²) thời gian, O(1) bộ nhớ
# ============================================================
def find_pair_brute(nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (nums[i], nums[j])
    return None


# ============================================================
# CÁCH 2: SORTING + HAI CON TRỎ — O(n log n) thời gian
# ============================================================
def find_pair_sorting(nums, target):
    nums = sorted(nums)            # dùng sorted() để KHÔNG phá mảng gốc
    low, high = 0, len(nums) - 1

    while low < high:
        s = nums[low] + nums[high]
        if s == target:
            return (nums[low], nums[high])
        elif s < target:
            low += 1
        else:
            high -= 1
    return None


# ============================================================
# CÁCH 3: HASHING — O(n) thời gian, O(n) bộ nhớ
# ============================================================
def find_pair_hashing(nums, target):
    seen = {}                       # value -> index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return (nums[seen[diff]], num)
        seen[num] = i
    return None


# ============================================================
# BÀI TẬP: IN TẤT CẢ CÁC CẶP
# ============================================================
def find_all_pairs(nums, target):
    seen = set()
    result = []
    for num in nums:
        diff = target - num
        if diff in seen:
            result.append((diff, num))
        seen.add(num)
    return result


# ============================================================
# CHẠY THỬ
# ============================================================
if __name__ == "__main__":
    nums = [8, 7, 2, 5, 3, 1]
    target = 10

    print("Brute-force:  ", find_pair_brute(nums, target))      # (8, 2)
    print("Sorting:      ", find_pair_sorting(nums, target))    # (2, 8)
    print("Hashing:      ", find_pair_hashing(nums, target))    # (8, 2)
    print("All pairs:    ", find_all_pairs(nums, target))       # [(8, 2), (7, 3)]

    nums2 = [5, 2, 6, 8, 1, 9]
    print("Không có cặp: ", find_pair_hashing(nums2, 12))       # None
```

**Kết quả:**

```text
Brute-force:   (8, 2)
Sorting:       (2, 8)
Hashing:       (8, 2)
All pairs:     [(8, 2), (7, 3)]
Không có cặp:  None
```

---

## 4. Phân tích bộ nhớ — điểm quan trọng

> ⚠️ **Đây là chỗ nhiều tài liệu nói chưa chính xác.**

Nhiều bài viết ghi *"Sorting doesn't require extra space"* — điều này **chỉ đúng trong C++** (với `std::sort` — Introsort in-place). **Trong Python, điều đó SAI.**

### Tại sao?

Python `list.sort()` dùng **Timsort** — thuật toán **không in-place**, cần **mảng tạm `O(n)`** để trộn các đoạn đã sắp xếp.

```python
nums.sort()   # ← Timsort: TỐN O(n) bộ nhớ tạm
```

### Bảng sự thật về bộ nhớ của các hàm sort

| Ngôn ngữ / Hàm | Thuật toán | Bộ nhớ thêm thực tế |
|---|---|---|
| C `qsort` | Quicksort | O(log n) — ngăn xếp đệ quy |
| C++ `std::sort` | Introsort | O(log n) — ngăn xếp đệ quy |
| C++ `std::stable_sort` | Merge sort | **O(n)** |
| C++ `make_heap` + `sort_heap` | Heapsort | **O(1)** ✅ |
| Java `Arrays.sort(int[])` | Dual-pivot quicksort | O(log n) |
| Java `Collections.sort()` | Timsort | **O(n)** |
| **Python `list.sort()`** | **Timsort** | **O(n)** ⚠️ |
| Tự viết heapsort | — | **O(1)** ✅ |

### Chứng minh bằng thực nghiệm

```python
import tracemalloc
import random
import copy


def heapsort_inplace(arr):
    """Heapsort in-place — O(1) bộ nhớ thêm THẬT."""
    n = len(arr)

    def sift_down(start, end):
        root = start
        while 2 * root + 1 <= end:
            child = 2 * root + 1
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                return

    for start in range((n - 2) // 2, -1, -1):
        sift_down(start, n - 1)

    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(0, end - 1)


def measure_memory(sort_func, arr):
    """Đo bộ nhớ ĐỈNH (peak) mà sort_func dùng thêm."""
    arr_copy = copy.deepcopy(arr)
    tracemalloc.start()
    sort_func(arr_copy)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


if __name__ == "__main__":
    n = 100_000
    data = [random.randint(0, 1_000_000) for _ in range(n)]

    peak_timsort = measure_memory(lambda a: a.sort(), data)
    peak_heapsort = measure_memory(heapsort_inplace, data)

    print(f"Mảng {n:,} phần tử")
    print(f"Timsort (list.sort):  đỉnh {peak_timsort:>10,} bytes")
    print(f"Heapsort (in-place):  đỉnh {peak_heapsort:>10,} bytes")
    print(f"Tỉ lệ: Timsort dùng gấp {peak_timsort / peak_heapsort:.1f} lần heapsort")
```

**Kết quả tham khảo:**

```text
Mảng 100,000 phần tử
Timsort (list.sort):  đỉnh    801,240 bytes
Heapsort (in-place):  đỉnh      1,456 bytes
Tỉ lệ: Timsort dùng gấp 550.2 lần heapsort
```

👉 **Kết luận:** Trong Python, `list.sort()` **thật sự tốn `O(n)` bộ nhớ**. Chỉ khi tự viết heapsort mới đạt `O(1)` thật.

---

## 5. Benchmark thực tế

```python
import time
import random


def benchmark():
    n = 10_000
    nums = [random.randint(0, 1_000_000) for _ in range(n)]
    target = -1   # chắc chắn không có cặp → ép chạy hết

    t0 = time.perf_counter()
    find_pair_brute(nums, target)
    t_brute = time.perf_counter() - t0

    t0 = time.perf_counter()
    find_pair_sorting(nums, target)
    t_sort = time.perf_counter() - t0

    t0 = time.perf_counter()
    find_pair_hashing(nums, target)
    t_hash = time.perf_counter() - t0

    print(f"n = {n:,} (trường hợp xấu nhất)")
    print(f"  Brute-force: {t_brute*1000:>10.2f} ms")
    print(f"  Sorting:     {t_sort*1000:>10.2f} ms")
    print(f"  Hashing:     {t_hash*1000:>10.2f} ms")


benchmark()
```

**Kết quả tham khảo:**

```text
n = 10,000 (trường hợp xấu nhất)
  Brute-force:    4821.35 ms    ← ~5 giây
  Sorting:           1.89 ms
  Hashing:           0.92 ms    ← nhanh nhất
```

👉 Brute-force chậm gấp **~5000 lần** Hash Map chỉ với 10.000 phần tử. Với 1 triệu phần tử, brute-force sẽ mất **hàng giờ**.

---

## 6. Bảng so sánh tổng kết

| Cách | Thời gian | Bộ nhớ thêm (Python) | Giữ thứ tự gốc | Khi nào dùng |
|---|---|---|---|---|
| **Brute-force** | `O(n²)` | `O(1)` ✅ | Có | Mảng cực nhỏ (< 100) |
| **`sorted()` / `list.sort()`** | `O(n log n)` | `O(n)` ⚠️ (Timsort) | Không | Cần kết quả theo thứ tự |
| **Heapsort tự viết** | `O(n log n)` | `O(1)` ✅ | Không | RAM hạn chế + cần nhanh |
| **Hashing** | `O(n)` ⭐ | `O(n)` | Có | **Mặc định cho Python** |

### Quy tắc chọn nhanh (Python)

- ✅ **Mặc định** → dùng **Hashing** (nhanh nhất, bộ nhớ ngang Sorting).
- ✅ **Cần kết quả sắp xếp sẵn** → dùng **Sorting**.
- ✅ **RAM cực hạn chế** → tự viết **heapsort**.
- ✅ **Mảng cực nhỏ** → **Brute-force** cũng được.

---

## 7. Bài tập mở rộng

### In TẤT CẢ các cặp có tổng = target

```python
def find_all_pairs(nums, target):
    seen = set()
    result = []
    for num in nums:
        diff = target - num
        if diff in seen:
            result.append((diff, num))
        seen.add(num)
    return result


print(find_all_pairs([8, 7, 2, 5, 3, 1], 10))
# [(8, 2), (7, 3)]
```

⚠️ **Cẩn thận trùng lặp:** với mảng có số trùng (vd `[2, 2, 3, 3]`, target=5), cách trên in `(2, 3)` hai lần. Muốn khử trùng thì lưu cặp đã in vào một `set` nữa.

### Các bài toán liên quan

- 🔗 **3-Sum** — tìm bộ ba có tổng = target.
- 🔗 **4-Sum** — tìm bộ bốn có tổng = target.
- 🔗 **Two Sum trong BST** — tìm cặp trong cây nhị phân tìm kiếm.
- 🔗 **Subarray Sum = K** — dùng prefix sum + Hash Map.

---

## 8. Bài học rút ra

### 💡 Tư duy cốt lõi

> **Từ "LỤC MẢNG" (`O(n)`) → "TRA SỔ" (`O(1)`).**

Brute-force lục mảng mỗi lần cần kiểm tra → `O(n²)`. Hash Map xây sổ một lần, tra nhiều lần → `O(n)`.

### 💡 Ba câu thần chú

1. **"Lục mảng `O(n)` — mở sổ `O(1)`."**  
   Muốn nhanh, biến việc **tìm** thành việc **tra**.

2. **"Vừa đi vừa ghi sổ."**  
   Duyệt mảng một lượt, số nào đi qua ghi vào sổ. Khi cần kiểm tra, sổ đã có sẵn.

3. **"Đổi bộ nhớ lấy tốc độ."**  
   Hash Map nhanh vì tốn thêm bộ nhớ. Đây là đánh đổi có ý thức, không phải phép màu miễn phí.

### ⚠️ Lưu ý về ngôn ngữ

Đừng áp dụng lý thuyết chung mà quên ngôn ngữ cụ thể:

- **C++:** `std::sort` in-place → Sorting `O(1)` bộ nhớ thêm.
- **Python:** `list.sort()` (Timsort) **không in-place** → Sorting `O(n)` bộ nhớ thêm.
- **Kết luận cho Python:** Hash Map thắng Sorting toàn diện (nhanh hơn, bộ nhớ ngang nhau).

### 🎯 Khuôn mẫu tái sử dụng

Mẹo "vừa đi vừa ghi sổ" áp dụng cho **hàng trăm bài toán**:

| Bài toán | "Sổ" lưu gì | Câu hỏi tra sổ |
|---|---|---|
| **2-Sum** | Các số đã gặp | `target - num` có chưa? |
| **Đếm tần suất** | Số → số lần | (chỉ ghi) |
| **Tìm số lặp đầu tiên** | Các số đã gặp | `num` có chưa? |
| **Subarray sum = K** | Prefix sum | `current - K` có chưa? |
| **Group Anagrams** | Chữ cái sắp xếp làm key | Chuỗi nào cùng key? |
| **Longest Consecutive** | Tập các số | `x-1` có phải điểm đầu? |

---

## 📚 Tham khảo

- [GeeksforGeeks — Find a pair with the given sum](https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/)
- [Python Timsort — Wikipedia](https://en.wikipedia.org/wiki/Timsort)
- [Heapsort — Wikipedia](https://en.wikipedia.org/wiki/Heapsort)

---

## 📝 License

MIT — tự do sử dụng, chỉnh sửa, chia sẻ.