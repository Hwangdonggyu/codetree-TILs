def bubble_sort(arr):
    for i in range(n):
        for j in range(n-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

n = int(input())
input_str = input("").strip()  # 입력값 양 끝의 공백 제거
if input_str:
    arr = list(map(int, input_str.split(" ")))
# arr = list(map(int,input("").split(" ")))
arr = bubble_sort(arr)
for i in range(n):
    print(arr[i],end=" ")