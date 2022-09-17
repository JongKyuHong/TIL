import sys
import heapq
input = sys.stdin.readline

n = int(input())
INF = sys.maxsize
graph = [[INF]*(n+1) for _ in range(n+1)]
while 1:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                

res = []
value = 0
for i in range(1, n+1):
    res.append(max(graph[i][1:]))
m = min(res)
print(m, res.count(m))
for i in res:
    if i == m:
        print(i, end=' ')
    
    


