import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = float('inf')
lst = [[INF]*(n+1) for _ in range(n+1)]
path = [[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            lst[i][j] = 0
            path[i][j] = INF

for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a][b] = c
    lst[b][a] = c
    path[a][b] = b
    path[b][a] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if lst[i][j] > lst[i][k] + lst[k][j]:
                lst[i][j] = lst[i][k] + lst[k][j]
                path[i][j] = path[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if path[i][j] == INF:
            print('-',end=' ')
        else:
            print(path[i][j], end=' ')
    print()