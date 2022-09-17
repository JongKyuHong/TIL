import sys
input = sys.stdin.readline
INF = float('inf')
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

max_v = INF
idx = 0
for i in range(1, n+1):
    if max_v > sum(graph[i][1:]):
        max_v = sum(graph[i][1:])
        idx = i
print(idx)