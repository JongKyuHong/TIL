import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s, t = map(int, input().split())
dist = [INF] * (n+1)
q = [[0, s]]
while q:
    cost, now = heapq.heappop(q)
    if dist[now] < cost:
        continue
    for next_node, next_dist in graph[now]:
        d = cost + next_dist
        if dist[next_node] > d:
            dist[next_node] = d
            heapq.heappush(q, (d, next_node))

print(dist[t])