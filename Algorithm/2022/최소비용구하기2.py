import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())

q = [[0, start, [start]]]
dist = [sys.maxsize] * (n+1)
dist_path = [[] for _ in range(n+1)]
dist[start] = 0
while q:
    now_dist, now, path = heapq.heappop(q)
    if dist[now] < now_dist:
        continue
    for next_node, next_dist in graph[now]:
        d = next_dist + now_dist
        if dist[next_node] > d:
            dist[next_node] = d
            dist_path[next_node] = path + [next_node]
            heapq.heappush(q,(d, next_node, dist_path[next_node]))

print(dist[end])
print(len(dist_path[end]))
print(dist_path[end])