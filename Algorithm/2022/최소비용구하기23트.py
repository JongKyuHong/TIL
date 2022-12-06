import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append((b,c))

start, end = map(int, input().split())
cnt = 0
dist_path = [[] for _ in range(n+1)]


def dijkstra(start):
    dist[start] = 1
    q = [[0, start,[start]]]
    while q:
        cost, node, path = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for next_node, next_cost in bus[node]:
            d = next_cost + cost
            if dist[next_node] > d:
                dist[next_node] = d
                dist_path[next_node] = path + [next_node]
                heapq.heappush(q, (d, next_node, dist_path[next_node]))

dist = [float('inf')] * (n+1)
dijkstra(start)
print(dist[end])
print(len(dist_path[end]))
print(*dist_path[end])