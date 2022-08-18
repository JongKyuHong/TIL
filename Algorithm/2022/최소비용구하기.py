import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())

def dijkstra(start):
    q = [[0, start]]
    dist = [INF] * (n+1)
    dist[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for next_node, next_dist in graph[now]:
            d = cost + next_dist
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, (d, next_node))

    return dist

dist_x = dijkstra(start)
print(dist_x[end])