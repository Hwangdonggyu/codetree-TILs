def selection_sort(n, m):
    for i in range(n - 1, 0, -1):
        a = max_index(i + 1, m)
        m[a], m[i] = m[i], m[a]
    
    for i in range(n):
        print(m[i], end=" ")

def max_index(n, m):
    max_i = 0
    for i in range(1, n):
        if m[max_i] < m[i]:
            max_i = i
    return max_i

n = int(input())
m = list(map(int, input().split()))
selection_sort(n, m)