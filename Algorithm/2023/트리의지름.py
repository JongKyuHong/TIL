import heapq
import sys
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    lst = list(map(int, input().split()))
    node = lst[0]
    lst = lst[1:-1]
    for i in range(0, len(lst), 2):
        graph[node].append((lst[i+1],lst[i]))
        
ans = 0
visited = [0]*(V+1)
visited[1] = 1
def bfs(start):
    global ans
    q = [[0, start]]
    dist = [float('inf')]*(V+1)
    dist[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for next_cost, next_node in graph[node]:
            d = next_cost + cost
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, [d, next_node])
    return dist
dist = bfs(1)
dist = bfs(dist.index(max(dist[1:])))
print(max(dist[1:]))