import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
s, e = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    h1,h2,k = map(int, input().split())
    graph[h1].append((k,h2))
    graph[h2].append((k,h1))

p = []
dist = [0]*(N+1)
def dijkstra(start):
    q = [[-float('inf'), start]]
    dist[start] = float('inf')
    while q:
        cost, node = heapq.heappop(q)
        cost = -cost
        if dist[node] > cost:
            continue
        for next_cost, next_node in graph[node]:
            tmp = min(cost, next_cost)
            if dist[next_node] < tmp:
                dist[next_node] = tmp
                heapq.heappush(q, (-tmp, next_node))
dijkstra(s)
print(dist[e])