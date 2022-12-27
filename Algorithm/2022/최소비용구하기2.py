import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())

def dijkstra(start):
    path = [start]
    q = [[0, start, path]]
    dist[start] = 0
    while q:
        cost, now, path = heapq.heappop(q)
        if now == end:
            return path
        if dist[now] < cost:
            continue
        for next_node, next_dist in graph[now]:
            d = next_dist + cost
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, (d, next_node, path+[next_node]))
            
INF = float('inf')
dist = [INF]*(n+1)
path = dijkstra(start)
print(dist[end])
print(len(path))
print(*path)