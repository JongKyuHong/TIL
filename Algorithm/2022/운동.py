import sys
input = sys.stdin.readline

v, e = map(int, input().split())
INF = float('inf')
graph = [[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

res = INF
for i in range(1,v+1):
    if graph[i][i] == INF:
        continue    
    res = min(res,graph[i][i])
print(-1) if res == INF else print(res)