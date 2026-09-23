nums = [5,4,2,6,1]


def binary_search(arr, x):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def count_smaller(nums):
    sorted = []
    counts = []
    for x in reversed(nums):
        pos = binary_search(sorted, x)
        counts.append(pos)
        sorted.insert(pos, x)
    counts.reverse()
    return counts


print(count_smaller(nums))
