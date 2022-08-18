from dis import dis
import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
n, m = map(int, input().split())
ward = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().split()) # a분기점, b분기점 지나는데 t만큼 시간이 든다.
    graph[a].append((b,t))
    graph[b].append((a,t))

q = [[0, 0]]
distance = [INF]*n
distance[0] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for next_node, next_dist in graph[now]:
        if ward[next_node] == 0 or next_node == n-1:
            d = dist+next_dist
            if distance[next_node] > d:
                distance[next_node] = d
                heapq.heappush(q, (d, next_node))

if distance[n-1] == INF:
    print(-1)
else:
    print(distance[n-1])
