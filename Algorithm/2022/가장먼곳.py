import sys
import heapq
import time
start = time.time() 

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
a, b, c= map(int, input().split())

graph = [[] for _ in range(N+1)]
M = int(input())

for _ in range(M):
    d, e, l = map(int, input().split())
    graph[d].append([e,l])
    graph[e].append([d,l])

def dijkstra(graph,i):
    INF = int(10e9)
    dist = [INF] * len(graph)
    dist[i] = 0
    q = [[i, 0]]
    while q:
        now, value = heapq.heappop(q)
        if dist[now] != value:
            continue
        for next_node, next_dist in graph[now]:
            cost = value + next_dist
            if dist[next_node] > cost:
                dist[next_node] = cost
                heapq.heappush(q,[next_node,cost])
    return dist


dist_a = dijkstra(graph, a)
dist_b = dijkstra(graph, b)
dist_c = dijkstra(graph, c)

max_v = 0
max_i = 0
for i in range(1,N+1):
    if max_v < min(dist_a[i], dist_b[i], dist_c[i]):
        max_v = min(dist_a[i], dist_b[i], dist_c[i])
        max_i = i
print(max_i)
print("time :", time.time() - start)