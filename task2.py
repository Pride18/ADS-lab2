arr = [0, 1, 2, 1, 4, 5, 3]


def binary_search(arr):
    if len(arr) < 3:
        return "Массив не горный"
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2 # середина
        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # идём вверх
        else:
            right = mid  # идём вниз

    # Пик не должен быть на краю
    if left == 0 or left == len(arr) - 1:
        return "Массив не горный"

    return f"Массив горный, пик - {left}"
print(binary_search(arr))
