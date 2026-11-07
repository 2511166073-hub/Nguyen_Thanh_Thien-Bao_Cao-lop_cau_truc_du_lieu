import math

def jump_search(arr, x):
    n = len(arr)

    if n == 0:
        return -1

    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))

        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i

    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    x = 13

    result = jump_search(arr, x)

    if result != -1:
        print(f"Tìm thấy {x} tại vị trí {result}")
    else:
        print(f"Không tìm thấy {x}")