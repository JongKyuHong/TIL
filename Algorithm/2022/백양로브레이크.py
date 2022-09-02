import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a][b] = t

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

for i in range(n):
    graph[i][i] = 0
k = int(input())
s = list(map(int, input().split()))

res = []
res_v = INF
for i in range(1,n+1):
    s1 = []
    for j in s:
        s1.append(graph[j][i]+graph[i][j])
    if res_v > max(s1):
        res_v = max(s1)
        res = [i]
    elif res_v == max(s1):
        res.append(i)

print(*sorted(res))
