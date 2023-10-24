import sys 
import heapq
input = sys.stdin.readline
INF = float('inf')

N, M, K = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    lst[start].append((time, end))
    lst[end].append((time, start))

q = []
heapq.heappush(q, (0, 1, K))
dist = [[INF]*(K+1) for _ in range(N+1)]
dist[1][K] = 0

while q:
    cost, node, tmp = heapq.heappop(q)
    if node == N:
        continue
    for next_cost, next_node in lst[node]:
        d = next_cost + cost
        if dist[next_node][tmp] > d:
            dist[next_node][tmp] = d
            heapq.heappush(q, (d, next_node, tmp))
        if tmp > 0 and dist[next_node][tmp-1] > cost:
            dist[next_node][tmp-1] = min(dist[next_node][tmp-1], cost)
            heapq.heappush(q, (cost, next_node, tmp-1))
print(min(dist[N]))