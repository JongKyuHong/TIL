import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
def dijkstra(start):
    q = [[0,start]]
    dist = [INF]*(N+1)
    dist[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for next_cost, next_node in tree[node]:
            d = next_cost + cost
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q,(d, next_node))
    return dist
N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((c,b))
    tree[b].append((c,a))
    
for _ in range(M):
    a, b = map(int, input().split())
    dist = dijkstra(a)
    print(dist[b])
