import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
a, b, c= map(int, input().split())

graph = [[] for _ in range(N+1)]
M = int(input())

for _ in range(M):
    d, e, l = map(int, input().split())
    graph[d].append([e,l])
    graph[e].append([d,l])

def dijkstra(graph,start):
    INT_MAX = int(10e9)
    distance = [INT_MAX] * len(graph)
    distance[start] = 0
    heap = [[0, start]]
    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] != dist:
            continue
        for next_node, next_dist in graph[node]:
            if dist + next_dist < distance[next_node]:
                distance[next_node] = dist + next_dist
                heapq.heappush(heap, [distance[next_node], next_node])
    return distance




max_v = 0
max_i = 0
dist_a = dijkstra(graph, a)
dist_b = dijkstra(graph, b)
dist_c = dijkstra(graph, c)


for i in range(1,N+1):
    if max_v < min(dist_a[i], dist_b[i], dist_c[i]):
        max_v = min(dist_a[i], dist_b[i], dist_c[i])
        max_i = i
print(max_i)
