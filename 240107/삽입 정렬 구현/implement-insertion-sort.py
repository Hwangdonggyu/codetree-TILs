def insertion_sort(arr):
  size = len(arr)
  for i in range(size):
    j = i - 1 
    key = arr[i]
    while (j >= 0 and arr[j]) > key:
      arr[j + 1] = arr[j]
      j-= 1
    arr[j + 1] = key
  return arr

n = int(input())
m = list(map(int,input().split()))
m = insertion_sort(m)
for i in range(n):
    print(m[i], end = " ")