import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
start,end = map(int, input().split())
q = [[0, start]]
dist = [float('inf')]*(N+1)
dist[start] = 0
while q:
    cost, node = heapq.heappop(q)
    if dist[node] < cost:
        continue
    for next_cost, next_node in graph[node]:
        c = cost+next_cost
        if dist[next_node] > c:
            dist[next_node] = c
            heapq.heappush(q,(c, next_node))
print(dist[end])