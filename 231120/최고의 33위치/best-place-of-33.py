n = int(input())
a = []
max_count = []
for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(n-2):
    for w in range(n-2):
        count = 0
        for x in range(i,i+3):
            for y in range(w,w+3):
                count += a[x][y]
        max_count.append(count)
print(max(max_count))