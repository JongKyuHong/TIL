import sys 
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF]*(V+1)
    dist[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        for next_cost, next_node in lst[node]:
            d = cost+next_cost
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, (d, next_node))
    return dist

V, E = map(int, input().split())
K = int(input())
lst = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    lst[u].append((w, v))

dist = dijkstra(K)

for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])

