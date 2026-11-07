def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i          # tìm thấy, trả về vị trí
    return "không tìm thấy"                # không tìm thấy

# Ví dụ
A = [5, 2, 8, 1, 9]
print(linear_search(A, 9))   # 4
print(linear_search(A, 7))   # "không tìm thấy"
print(A[3])  