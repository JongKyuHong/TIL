import sys 
input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())
lst = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    if lst[start][end] > cost:
        lst[start][end] = cost

for i in range(1, n+1):
    lst[i][i] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        for k in range(1, n+1):
            if j == k or i == k:
                continue
            if lst[j][k] > lst[j][i] + lst[i][k]:
                lst[j][k]  = lst[j][i] + lst[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if lst[i][j] == INF:
            lst[i][j] = 0
        print(lst[i][j], end=' ')
    print()

