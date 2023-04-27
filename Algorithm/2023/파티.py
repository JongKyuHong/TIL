import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
edge = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edge[a].append((c, b))

def dijkstra(start):
    q = [[0, start]]
    dist = [float('inf')]*(N+1)
    dist[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for next_cost, next_node in edge[node]:
            c = cost+next_cost
            if dist[next_node] > c:
                dist[next_node] = c
                heapq.heappush(q, [c, next_node])
    return dist

res = [0]*(N+1)
for i in range(1, N+1):
    d = dijkstra(i)
    res[i] += d[X]
    d = dijkstra(X)
    res[i] += d[i]

print(max(res))