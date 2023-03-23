import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for l, e in graph[now]:
            cost = l + dist
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (cost, e))

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
distance = [INF]*(D+1)
for i in range(D):
    graph[i].append((1,i+1))
for _ in range(N):
    start, end, length = map(int, input().split())
    if end > D:
        continue
    graph[start].append((length, end))

dijkstra(0)
print(distance[D])