arr = [0, 1, 2, 3, 4, 6, 7, 8] # отсортированный массив
n = int(input())
order = True if arr[0] < arr[-1] else False # проверка на прямой или обратный порядок
def binary_search(arr, n):
  left = 0 # левая граница
  right = len(arr) - 1 # правая граница
  while left <= right:
    mid = (left + right) // 2 # середина
    if arr[mid] == n:
      return "Число найдено"
    elif arr[mid] > n and order:
      right = mid - 1
    elif arr[mid] < n and not order:
      right = mid - 1
    elif arr[mid] < n and order:
      left = mid + 1
    elif arr[mid] > n and not order:
      left = mid + 1
  arr.insert(left, n) # добавляем число, если не нашли его в массиве
  return "Число не найдено, поэтому оно добавлено в массив"

print(binary_search(arr, n))
print(arr)
