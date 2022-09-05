import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
dist = [sys.maxsize] * (n+1)
parent = [0] * (n+1)
def dijkstra(v):
    q = [[0, v]]
    dist[v] = 0
    while q:
        now_dist, now = heapq.heappop(q)
        if dist[now] < now_dist:
            continue
        for next_node, next_dist in graph[now]:
            d = next_dist + now_dist
            if dist[next_node] > d:
                dist[next_node] = d
                parent[next_node] = now
                heapq.heappush(q,(d, next_node))
    
dijkstra(start)

ans = []
tmp = end
while tmp != start:
    ans.append(str(tmp))
    tmp = parent[tmp]

ans.append(str(start))
ans.reverse()

print(dist[end])
print(len(ans))
print(' '.join(ans))