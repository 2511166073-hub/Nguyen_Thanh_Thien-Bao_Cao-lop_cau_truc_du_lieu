# BÁO CÁO: DUYỆT CÂY THEO MỨC (LEVEL ORDER TRAVERSAL) — PYTHON

## Mục lục

1. [Tổng quan](#1-tổng-quan)
2. [Khái niệm và nguyên lý](#2-khái-niệm-và-nguyên-lý)
3. [Thuật toán cốt lõi](#3-thuật-toán-cốt-lõi)
4. [Minh họa từng bước](#4-minh-họa-từng-bước)
5. [Cài đặt Python cơ bản](#5-cài-đặt-python-cơ-bản)
6. [Biến thể: Duyệt theo từng level riêng biệt](#6-biến-thể-duyệt-theo-từng-level-riêng-biệt)
7. [Vấn đề mất thông tin cấu trúc](#7-vấn-đề-mất-thông-tin-cấu-trúc)
8. [Khôi phục quan hệ cha–con bằng null](#8-khôi-phục-quan-hệ-chacon-bằng-null)
9. [Mở rộng sang cây N phân (N-ary Tree)](#9-mở-rộng-sang-cây-n-phân-n-ary-tree)
10. [Serialize / Deserialize cây bằng Level Order](#10-serialize--deserialize-cây-bằng-level-order)
11. [Các biến thể nâng cao](#11-các-biến-thể-nâng-cao)
12. [Độ phức tạp](#12-độ-phức-tạp)
13. [So sánh BFS và DFS](#13-so-sánh-bfs-và-dfs)
14. [Lỗi thường gặp](#14-lỗi-thường-gặp)
15. [Kết luận](#15-kết-luận)

---

## 1. Tổng quan

**Level Order Traversal** (duyệt cây theo mức) là phương pháp duyệt cây **theo từng tầng**, từ trên xuống dưới, và trong mỗi tầng duyệt **từ trái sang phải**. Đây chính là **BFS (Breadth-First Search)** áp dụng trên cấu trúc cây.

Báo cáo này trình bày toàn bộ nội dung bằng **Python**, bao gồm:

- Nguyên lý và cách cài đặt level order trên **cây nhị phân**
- Vấn đề **mất thông tin cấu trúc** khi chỉ lưu giá trị theo tầng
- Cách **khôi phục quan hệ cha–con** bằng cách thêm `None`
- Mở rộng thuật toán sang **cây N phân** (N-ary tree)
- Serialize / Deserialize cây bằng level order
- Các biến thể nâng cao và độ phức tạp

---

## 2. Khái niệm và nguyên lý

### 2.1. Định nghĩa

Với cây nhị phân:

```
        1          ← level 0
       / \
      2   3        ← level 1
     / \   \
    4   5   6      ← level 2
```

Kết quả duyệt level order: **1, 2, 3, 4, 5, 6**

### 2.2. Nguyên lý hoạt động

BFS duyệt theo **chiều rộng** → cần cấu trúc dữ liệu **FIFO (vào trước ra trước)** → dùng **`collections.deque`** trong Python.

**Quy tắc:**

1. Node được thăm trước thì các con của nó được đưa vào queue trước
2. Nhờ vậy, các node ở cùng tầng được xử lý liên tiếp nhau
3. Tầng `d` luôn được xử lý xong trước khi sang tầng `d+1`

> **Lưu ý Python:** Dùng `collections.deque` thay vì `list` vì `deque.popleft()` là `O(1)`, còn `list.pop(0)` là `O(n)`.

---

## 3. Thuật toán cốt lõi

### 3.1. Mã giả

```
function level_order(root):
    if root is None: return

    q = empty deque
    q.append(root)

    while q is not empty:
        node = q.popleft()              # lấy node đầu queue
        process(node)                    # in / lưu giá trị

        if node.left  is not None: q.append(node.left)
        if node.right is not None: q.append(node.right)
```

### 3.2. Điểm mấu chốt

| Thao tác | Cấu trúc | Vai trò |
|----------|----------|---------|
| `q.append(x)` | Thêm vào **cuối** queue | Đưa con vào hàng chờ |
| `q.popleft()` | Lấy ra ở **đầu** queue — `O(1)` | Xử lý node theo thứ tự đến |
| Kiểm tra `is not None` trước khi append | Tránh đẩy node rỗng vào queue | Tiết kiệm bộ nhớ, tránh crash |

---

## 4. Minh họa từng bước

Với cây ví dụ ở mục 2.1:

| Bước | Queue (đầu → cuối) | Node lấy ra | Kết quả |
|------|---------------------|-------------|---------|
| 1 | `[1]` | 1 | 1 |
| 2 | `[2, 3]` | 2 | 1, 2 |
| 3 | `[3, 4, 5]` | 3 | 1, 2, 3 |
| 4 | `[4, 5, 6]` | 4 | 1, 2, 3, 4 |
| 5 | `[5, 6]` | 5 | 1, 2, 3, 4, 5 |
| 6 | `[6]` | 6 | 1, 2, 3, 4, 5, 6 |
| 7 | `[]` | — | Hoàn tất |

**Nhận xét:** Tại mỗi bước, queue luôn chứa các node của **tầng hiện tại** và **tầng kế tiếp**, theo đúng thứ tự trái → phải.

---

## 5. Cài đặt Python cơ bản

### 5.1. Định nghĩa node

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### 5.2. Duyệt level order — trả về list giá trị

```python
from collections import deque

def level_order(root):
    """Duyệt cây theo mức, trả về list giá trị theo thứ tự BFS."""
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        node = q.popleft()
        result.append(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return result
```

### 5.3. Chạy thử với cây ví dụ

```python
# Dựng cây:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(level_order(root))
# Output: [1, 2, 3, 4, 5, 6]
```

### 5.4. In theo từng dòng level

```python
def print_by_level(root):
    """In mỗi tầng trên một dòng."""
    if not root:
        return

    q = deque([root])

    while q:
        level_size = len(q)
        line = []
        for _ in range(level_size):
            node = q.popleft()
            line.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        print(line)

# Output:
# [1]
# [2, 3]
# [4, 5, 6]
```

---

## 6. Biến thể: Duyệt theo từng level riêng biệt

### 6.1. Yêu cầu

Trả về `List[List[int]]` — mỗi list con là giá trị của một tầng (LeetCode 102).

### 6.2. Kỹ thuật then chốt

> **Chốt `level_size = len(q)` ở đầu mỗi vòng lặp ngoài.**
> Đó chính là số node của tầng hiện tại. Vòng lặp trong xử lý **đúng `level_size` node** — tức là toàn bộ tầng hiện tại — trước khi chuyển sang tầng kế.

### 6.3. Cài đặt

```python
from collections import deque

def level_order_by_level(root):
    """Trả về List[List[int]] — mỗi list là một level."""
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)          # số node tầng hiện tại
        current_level = []

        for _ in range(level_size):  # xử lý đúng level_size node
            node = q.popleft()
            current_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(current_level)

    return result


# Với cây ví dụ:
print(level_order_by_level(root))
# Output: [[1], [2, 3], [4, 5, 6]]
```

### 6.4. Giải thích vòng lặp `for _ in range(level_size)`

- **Trước vòng for:** `level_size` được chốt = số node tầng hiện tại (ví dụ 2).
- **Trong vòng for:** pop 2 node (2 và 3), append con của chúng vào queue → queue bây giờ chứa toàn bộ node tầng sau.
- **Sau vòng for:** `current_level` có đủ giá trị tầng hiện tại; queue đã sẵn sàng cho tầng kế.
- **Sang vòng while tiếp:** `level_size` được chốt lại với giá trị mới.

---

## 7. Vấn đề mất thông tin cấu trúc

### 7.1. Phát biểu vấn đề

Output `[[1], [2, 3], [4, 5, 6]]` **KHÔNG cho biết** các node ở tầng dưới là con của ai.

**Lý do:** Khi không ghi `None`, thông tin "node này có con trái hay không" bị mất. Ví dụ:

- Node `3` có **con trái = None**, **con phải = 6**
- Nhưng output chỉ ghi `6` → không phân biệt được `6` là con trái hay con phải của `3`

### 7.2. Minh họa tính đa nghĩa

Hai cây **khác nhau** nhưng cho **cùng output** level order:

```
Cây A:                    Cây B:
    1                        1
   / \                      / \
  2   3                    2   3
 / \   \                  /   / \
4   5   6                4   5   6
```

| Cây | Level 0 | Level 1 | Level 2 |
|-----|---------|---------|---------|
| A | `[1]` | `[2, 3]` | `[4, 5, 6]` |
| B | `[1]` | `[2, 3]` | `[4, 5, 6]` |

→ **Cùng output, khác cấu trúc.** Vậy output "trơn" **không đủ** để tái tạo cây.

### 7.3. Kết luận

> Level order **không kèm `None`** = "điểm danh theo tầng" (biết ai ở tầng nào, **không biết ai là con ai**).

---

## 8. Khôi phục quan hệ cha–con bằng null

### 8.1. Ý tưởng

Ghi **cả `None`** vào output khi con vắng mặt:

```
Level 0: [1]
Level 1: [2, 3]
Level 2: [4, 5, None, 6]     ← None ở vị trí con trái của 3
```

Bây giờ quan hệ hiện ra rõ ràng nhờ **quy tắc vị trí**.

### 8.2. Quy tắc vị trí với cây nhị phân

> **Node ở vị trí `i` của level `k` có:**
> - **Con trái** ở vị trí `2i` của level `k+1`
> - **Con phải** ở vị trí `2i + 1` của level `k+1`

(0-indexed)

### 8.3. Áp dụng

| Node | Vị trí | Con trái (`2i`) | Con phải (`2i+1`) |
|------|--------|-----------------|-------------------|
| 2 | `i=0` | level 2 `[0]` = **4** | level 2 `[1]` = **5** |
| 3 | `i=1` | level 2 `[2]` = **None** | level 2 `[3]` = **6** |

→ Rõ ràng: `4, 5` là con của `2`; `6` là **con phải** của `3`. ✅

> Đây chính là cách **heap nhị phân** lưu cây trong mảng: `children(i) = 2i+1, 2i+2` (0-indexed). Level order + `None` = mảng heap.

### 8.4. Khi nào output "trơn" đủ dùng?

Chỉ khi đề cho thêm giả thiết:

- **Cây hoàn chỉnh (complete tree):** mọi tầng trừ tầng cuối đều đầy, tầng cuối lấp từ trái sang → áp dụng được quy tắc `2i, 2i+1`
- **Cây nhị phân tìm kiếm (BST):** dùng tính chất `left < node < right`
- **Đề cho kèm cây gốc**

### 8.5. Code minh họa ghi `None`

```python
from collections import deque

def level_order_with_none(root):
    """Ghi cả None cho node vắng mặt — dùng để tái tạo cây."""
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        current_level = []

        for _ in range(level_size):
            node = q.popleft()
            if node is None:
                current_level.append(None)
                continue

            current_level.append(node.val)
            q.append(node.left)     # luôn append cả 2, kể cả None
            q.append(node.right)

        result.append(current_level)

    return result


# Với cây ví dụ (node 3 chỉ có con phải):
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
print(level_order_with_none(root))
# Output: [[1], [2, 3], [4, 5, None, 6]]
```

---

## 9. Mở rộng sang cây N phân (N-ary Tree)

### 9.1. Khái niệm

- **Cây nhị phân (binary tree):** mỗi node **tối đa 2 con** (trái + phải)
- **Cây N phân / cây tổng quát (N-ary tree):** mỗi node có **bao nhiêu con cũng được** — 0, 1, 2, 3, 4,... tuỳ ý

→ Có 3 nhánh là **hoàn toàn hợp lệ** — đó là **cây tam phân (ternary tree)**, một dạng của N-ary tree.

### 9.2. Định nghĩa node N phân

```python
class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []
```

### 9.3. Level order trên cây N phân

```python
from collections import deque

def level_order_nary(root):
    """Duyệt cây N phân theo mức, trả về List[List[int]]."""
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        current_level = []

        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.val)

            for child in node.children:   # ← chỉ đổi chỗ này
                q.append(child)

        result.append(current_level)

    return result
```

→ Thuật toán **không đổi**: Queue + BFS + chốt `level_size` đầu mỗi vòng. Chỉ khác ở vòng `for child in node.children`.

### 9.4. Ví dụ cây tam phân

```
            1
         /  |  \
        2   3   4
       /|\
      5 6 7
```

```python
# Dựng cây tam phân
n1 = Node(1)
n2 = Node(2, [Node(5), Node(6), Node(7)])
n3 = Node(3)
n4 = Node(4)
n1.children = [n2, n3, n4]

print(level_order_nary(n1))
# Output: [[1], [2, 3, 4], [5, 6, 7]]
```

Tương tự cây nhị phân, output "trơn" **không cho biết** 5, 6, 7 là con của ai — cần kèm `None` để giải mã.

### 9.5. Quy tắc vị trí với cây N phân

> **Node ở vị trí `i` của level `k` → các con ở vị trí `k·i + 1`, `k·i + 2`, ..., `k·i + k` của level `k+1`**

| Loại cây | `k` | Vị trí các con của node `i` |
|----------|-----|----------------------------|
| Nhị phân | 2 | `2i+1, 2i+2` |
| **Tam phân** | **3** | **`3i+1, 3i+2, 3i+3`** |
| Tứ phân | 4 | `4i+1, 4i+2, 4i+3, 4i+4` |
| `k`-phân | `k` | `ki+1` … `ki+k` |

Số slot mỗi level khi serialize có `None`: **level `d` có `k^d` slot** (thay vì `2^d`).

**Ví dụ tam phân, mã hoá có `None`:**

```
Level 0: [1]                                              (1 slot)
Level 1: [2, 3, 4]                                        (3 slots)
Level 2: [5, 6, 7, None, None, None, None, None, None]    (9 slots)
```

Giải mã:

- Node `2` ở vị trí 0 → con ở `3·0+1, 3·0+2, 3·0+3` = vị trí 1,2,3 → trong level 2 (0-indexed) là **5, 6, 7** ✅
- Node `3` ở vị trí 1 → con ở `4,5,6` → toàn **None**
- Node `4` ở vị trí 2 → con ở `7,8,9` → toàn **None**

→ Rõ ràng 5, 6, 7 là con của **2**, không phải của 3 hay 4.

### 9.6. Ứng dụng thực tế của N-ary tree

| Ứng dụng | Số nhánh |
|----------|----------|
| **DOM tree** (HTML) | Mỗi thẻ có bao nhiêu thẻ con cũng được |
| **File system** (thư mục) | Mỗi thư mục chứa bao nhiêu file/folder cũng được |
| **Trie** (cây từ điển) | Mỗi node có tới 26 con (chữ cái) |
| **Cây tổ chức** (org chart) | Một sếp quản lý nhiều nhân viên |
| **Cây quyết định** (decision tree) | Tuỳ bài toán, có thể > 2 nhánh |
| **B-tree / B+ tree** (database index) | Mỗi node chứa hàng trăm khoá → hàng trăm con |
| **Cây cú pháp** (AST) | Một toán tử có thể có nhiều toán hạng |

### 9.7. Lưu ý khi chuyển từ binary → N-ary

| Điều gì đổi | Binary tree | N-ary tree |
|-------------|-------------|------------|
| Số con mỗi node | Cố định: 2 slot (`left`, `right`) | `list children` |
| Duyệt pre/in/post order | Có nghĩa rõ (giữa nằm giữa trái–phải) | **"In-order" mất nghĩa** → chỉ còn **pre-order** và **post-order** |
| Level order | Push `left`, `right` | Lặp `for child in children` |
| Serialize có `None` | Mỗi node 2 slot | Mỗi node `k` slot (hoặc dùng `len(children)`) |
| Công thức mảng `i` | `2i+1, 2i+2` | `ki+1 … ki+k` |

> **Lưu ý:** Với N-ary tree, **"in-order traversal" không còn định nghĩa được** — vì không có khái niệm "node nằm giữa con trái và con phải". Chỉ còn pre-order (node → các con) và post-order (các con → node).

---

## 10. Serialize / Deserialize cây bằng Level Order

### 10.1. Serialize

```python
from collections import deque

def serialize(root):
    """Chuyển cây thành list (level order có None)."""
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        node = q.popleft()

        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        q.append(node.left)
        q.append(node.right)

    # Cắt các None ở cuối cho gọn (tuỳ chọn)
    while result and result[-1] is None:
        result.pop()

    return result
```

### 10.2. Deserialize

```python
def deserialize(data):
    """Dựng lại cây từ list (level order có None)."""
    if not data or data[0] is None:
        return None

    root = TreeNode(data[0])
    q = deque([root])
    i = 1

    while q and i < len(data):
        node = q.popleft()

        # Con trái
        if i < len(data) and data[i] is not None:
            node.left = TreeNode(data[i])
            q.append(node.left)
        i += 1

        # Con phải
        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            q.append(node.right)
        i += 1

    return root
```

### 10.3. Kiểm tra round-trip

```python
# Cây:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

data = serialize(root)
print(data)
# [1, 2, 3, 4, 5, None, 6]

new_root = deserialize(data)
print(level_order(new_root))
# [1, 2, 3, 4, 5, 6]  ✅ round-trip thành công
```

---

## 11. Các biến thể nâng cao

### 11.1. Zigzag Level Order (LeetCode 103)

```python
def zigzag_level_order(root):
    if not root:
        return []

    q = deque([root])
    result = []
    left_to_right = True

    while q:
        level_size = len(q)
        current_level = deque()

        for _ in range(level_size):
            node = q.popleft()

            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)

            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)

        result.append(list(current_level))
        left_to_right = not left_to_right

    return result
```

### 11.2. Right View / Left View

```python
def right_view(root):
    """Lấy phần tử cuối cùng của mỗi level."""
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i == level_size - 1:      # node cuối level
                result.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)

    return result
```

### 11.3. Level Average

```python
def level_average(root):
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        total = 0
        for _ in range(level_size):
            node = q.popleft()
            total += node.val
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        result.append(total / level_size)

    return result
```

### 11.4. Minimum Depth

```python
def min_depth(root):
    """BFS — level đầu tiên gặp lá chính là độ sâu nhỏ nhất."""
    if not root:
        return 0

    q = deque([(root, 1)])      # (node, depth)

    while q:
        node, depth = q.popleft()

        if not node.left and not node.right:
            return depth

        if node.left:  q.append((node.left, depth + 1))
        if node.right: q.append((node.right, depth + 1))

    return 0
```

### 11.5. Tổng hợp biến thể

| Bài toán | Cách làm |
|----------|----------|
| **Zigzag Level Order** (LeetCode 103) | Duyệt level bình thường, level lẻ thì `appendleft` |
| **Right View / Left View** | Ở mỗi level, lấy phần tử cuối (right) hoặc đầu (left) |
| **Level Average / Max / Min** | Tính trên từng level trong vòng lặp `for level_size` |
| **Serialize / Deserialize cây** | BFS với queue, ghi `None` cho node rỗng |
| **Minimum Depth** | BFS — level đầu tiên gặp lá chính là độ sâu nhỏ nhất |
| **Connect Next Right Pointers** (LeetCode 116) | BFS, nối node cuối level với node đầu level kế |

---

## 12. Độ phức tạp

### 12.1. Cây nhị phân

- **Thời gian:** `O(N)` — mỗi node được thăm đúng 1 lần, mỗi thao tác `append`/`popleft` trên `deque` là `O(1)`
- **Không gian:** `O(W)` — với `W` là **số node lớn nhất trên một level** (độ rộng tối đa của cây)
  - Cây cân bằng: `W ≈ N/2` → `O(N)`
  - Cây lệch (skewed): `W = 1` → `O(1)`

### 12.2. Cây N phân

- **Thời gian:** `O(N)` — tương tự
- **Không gian:** `O(W)` — với `W` là **tổng số con tối đa tích luỹ trên một level**, có thể lớn hơn đáng kể so với cây nhị phân

### 12.3. Vì sao dùng `deque` mà không dùng `list`

```python
# ❌ Sai — O(n) mỗi lần pop đầu
lst = [1, 2, 3, 4]
lst.pop(0)          # O(n) → tổng BFS thành O(n²)

# ✅ Đúng — O(1) mỗi lần popleft
from collections import deque
q = deque([1, 2, 3, 4])
q.popleft()         # O(1) → tổng BFS thành O(n)
```

---

## 13. So sánh BFS và DFS

| Tiêu chí | BFS (Level Order) | DFS (Pre/In/Post) |
|----------|-------------------|-------------------|
| Cấu trúc | **`deque`** | **Stack / Đệ quy** |
| Thứ tự | Theo tầng | Theo nhánh sâu |
| Dùng khi | Tìm đường ngắn nhất, duyệt theo tầng | Kiểm tra cấu trúc, đường đi, subtree |
| Bộ nhớ | `O(W)` — độ rộng | `O(H)` — chiều cao |
| Ứng dụng | Shortest path, level views | Tree traversal, subtree check |

**Ví dụ DFS pre-order cùng cây:**

```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

print(preorder(root))
# [1, 2, 4, 5, 3, 6]
```

→ **BFS:** `[1, 2, 3, 4, 5, 6]` (theo tầng) — **DFS:** `[1, 2, 4, 5, 3, 6]` (theo nhánh sâu)

---

## 14. Lỗi thường gặp

1. **Quên kiểm tra `root is None`** → crash khi queue rỗng
2. **Không lưu `level_size` trước vòng `for`** → bị trộn lẫn các level
3. **Dùng `list` thay vì `deque`** → `pop(0)` là `O(n)`, tổng thành `O(n²)`
4. **Dùng `stack` thay vì `queue`** → thành DFS chứ không còn là level order
5. **Append con khi chưa kiểm tra `None`** → đẩy `None` vào queue, gây lỗi khi truy cập `.val`
6. **Nhầm lẫn "output trơn" với "output có `None`"** → không tái tạo được cây
7. **Với N-ary tree, quên vòng `for child in children`** → chỉ duyệt được con đầu tiên

---

## 15. Kết luận

> **Level Order = BFS trên cây = dùng `deque` + xử lý từng node, đẩy con trái rồi con phải vào cuối queue; muốn tách từng level thì "chốt" `level_size = len(q)` trước mỗi vòng `for`.**

**Tóm tắt các ý chính:**

- **Cây nhị phân:** push `left`, `right` — công thức vị trí `2i+1, 2i+2`
- **Cây N phân:** lặp `for child in children` — công thức vị trí `ki+1 … ki+k`
- **Output trơn `[[1],[2,3],[4,5,6]]`** không đủ tái tạo cây — cần thêm `None` để định vị con trái/phải
- **Serialize/Deserialize** dùng level order có `None` là cách phổ biến (LeetCode 297)
- **Luôn dùng `collections.deque`**, không dùng `list` cho queue
