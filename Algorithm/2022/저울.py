import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = float('inf')
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if i == j:
            continue
        if graph[i][j] == INF:
            if graph[j][i] == INF:
                cnt += 1
    print(cnt)
