def fibonacci_search(arr, x):
    n = len(arr)

    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1

    return -1


if __name__ == "__main__":
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    x = 85

    result = fibonacci_search(arr, x)

    if result != -1:
        print(f"Tìm thấy {x} tại vị trí {result}")
    else:
        print(f"Không tìm thấy {x}")