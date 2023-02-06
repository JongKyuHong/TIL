import sys
import heapq
input = sys.stdin.readline

p, w = map(int, input().split())
c, v = map(int, input().split())
graph = [[] for _ in range(p)]
for _ in range(w):
    start, end, width = map(int, input().split())
    graph[start].append((width, end))
    graph[end].append((width,start))

visited = [0]*p
q = []
heapq.heappush(q, (-float('inf'), c))
ans = float('inf')
while q:
    width, node = heapq.heappop(q)
    width *= -1
    if visited[node]:
        continue
    visited[node] = 1
    ans = min(ans, width)
    if node == v:
        print(ans)
        break
    for next_cost, next_node in graph[node]:
        heapq.heappush(q, (-next_cost, next_node))
        

