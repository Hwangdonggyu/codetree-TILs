from collections import deque

def radixSort(n, nums):
    buckets = [deque() for _ in range(10)]
    
    max_val = max(nums)
    queue = deque(nums)
    digit = 1  # 자릿수
    
    while max_val >= digit:  # 가장 큰 수의 자릿수일 때까지만 실행
        while queue:
            num = queue.popleft()
            buckets[(num // digit) % 10].append(num)  # 각 자리의 수(0~9)에 따라 버킷에 num을 넣는다.
        
        # 해당 자릿수에서 버킷에 다 넣었으면, 버킷에 담겨있는 순서대로 꺼내와 정렬한다.
        for bucket in buckets:
            while bucket:
                queue.append(bucket.popleft())

        digit *= 10  # 자릿수 증가시키기
    
    sorted_nums = list(queue)
    return sorted_nums

# 예시로 함수 호출
n = int(input())
nums = list(map(int, input().split()))
result = radixSort(n, nums)

for i in range(n):
    print(result[i], end=" ")