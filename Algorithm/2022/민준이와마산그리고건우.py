import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V,E,P = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(i):
    q = [[0, i]]
    dist = [INF] * (V+1)
    dist[1] = 0
    while q:
        now_dist, now = heapq.heappop(q)
        if dist[now] < now_dist:
            continue
        for next_node, next_dist in graph[now]:
            d = now_dist + next_dist
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q,(d, next_node))
    return dist
st = dijkstra(1)
st1 = dijkstra(P)
if st[P] + st1[V] == st[V]:
    print('SAVE HIM')
else:
    print('GOOD BYE')