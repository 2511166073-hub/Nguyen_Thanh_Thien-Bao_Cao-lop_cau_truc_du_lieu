def binary_search(arr, x):
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid            # tìm thấy
        elif arr[mid] < x:
            left = mid + 1        # tìm nửa phải
        else:
            right = mid - 1       # tìm nửa trái
    return 'không tìm thấy'                     # không tìm thấy

# Ví dụ (mảng PHẢI sắp xếp)
A = [1, 2, 5, 8, 9]
print(binary_search(A, 8))   # 3
print(binary_search(A, 7))   # không tìm thấy