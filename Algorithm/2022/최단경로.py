import sys
import heapq
input = sys.stdin.readline

INF = float('inf')

v, e = map(int, input().split())
graph = [[]*(v+1) for _ in range(v+1)]
k = int(input())

distance = [INF]*(v+1)
distance[k] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(v):
    q = []
    heapq.heappush(q, (0,v))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for end, value in graph[now]:
            cost = dist + value
            if cost < distance[end]:
                distance[end] = cost
                heapq.heappush(q, (cost, end))

dijkstra(k)

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])