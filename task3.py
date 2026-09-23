arr = [-4, -3, -2, -1, 8, 9, 10]


def binary_search(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2 # середина
        if arr[mid] < 0:
            left = mid + 1
        else:
            right = mid

    if len(arr) - left > left:
        return f'Положительных чисел больше - {len(arr) - left}'
    elif len(arr) - left == left:
        return f'Чисел поровну - {left}'
    else:
        return f'Отрицательных чисел больше - {left}'
print(binary_search(arr))
