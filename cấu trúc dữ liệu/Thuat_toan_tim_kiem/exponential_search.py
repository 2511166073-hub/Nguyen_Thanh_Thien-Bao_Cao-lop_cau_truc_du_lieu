def binary_search(arr, left, right, x):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def exponential_search(arr, x):
    n = len(arr)

    if n == 0:
        return -1

    if arr[0] == x:
        return 0

    i = 1

    while i < n and arr[i] <= x:
        i *= 2

    return binary_search(arr, i // 2, min(i, n - 1), x)


if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    x = 19

    result = exponential_search(arr, x)

    if result != -1:
        print(f"Tìm thấy {x} tại vị trí {result}")
    else:
        print(f"Không tìm thấy {x}")