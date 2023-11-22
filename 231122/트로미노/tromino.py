n,m = map(int,input().split(" "))

arr = [list(map(int, input().split())) for _ in range(n)]

max_sum =[]

# ㄴ자
max_val = 0
for i in range(n-1):
    for j in range(m-1):
        if max_val < arr[i][j]+arr[i+1][j]+arr[i+1][j+1]:
            max_val = arr[i][j]+arr[i+1][j]+arr[i+1][j+1]
max_sum.append(max_val)

# ㅡl자
max_val = 0
for i in range(n-1):
    for j in range(m-1):
        if max_val < arr[i+1][j]+arr[i+1][j]+arr[i+1][j+1]:
            max_val = arr[i+1][j]+arr[i+1][j]+arr[i+1][j+1]
max_sum.append(max_val)

# ㅣ-자
max_val = 0
for i in range (n-1):
    for j in range (m-1):
        if max_val < arr[i][j]+arr[i+1][j]+arr[i][j+1]:
            max_val = arr[i][j]+arr[i+1][j]+arr[i][j+1]
max_sum.append(max_val)

# ㄱ자
max_val = 0
for i in range(n-1):
    for j in range (m-1):
        if max_val < arr[i][j]+arr[i][j+1]+arr[i+1][j+1]:
            max_val = arr[i][j]+arr[i][j+1]+arr[i+1][j+1]
max_sum.append(max_val)

# ---자
max_val = 0
for i in range(n):
    for j in range (m-2):
        if max_val < arr[i][j]+arr[i][j+1]+arr[i][j+2]:
            max_val = arr[i][j]+arr[i][j+1]+arr[i][j+2]
max_sum.append(max_val)

# ㅣ자
max_val = 0
for i in range(n-2):
    for j in range (m):
        if max_val < arr[i][j]+arr[i+1][j]+arr[i+2][j]:
            max_val = arr[i][j]+arr[i+1][j]+arr[i+2][j]
max_sum.append(max_val)

print(max(max_sum))