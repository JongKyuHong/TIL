import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
costs = []
for _ in range(m):
    x,y,z = map(int, input().split()) 
    graph[x].append((y,z))
    graph[y].append((x,z))
    costs.append(z)

def dijkstra(mid):
    q = [[0, a]]
    dist = [INF]*(n+1)
    dist[a] = 0
    while q:
        now_cost, node = heapq.heappop(q)
        if dist[node] < now_cost:
            continue
        for next_node, next_cost in graph[node]:
            if next_cost > mid:
                continue
            if dist[next_node] > now_cost + next_cost:
                dist[next_node] = now_cost + next_cost
                heapq.heappush(q, (now_cost+next_cost, next_node))
    return dist[b] <= c

costs.sort()
left = 0
right = len(costs)-1
ans = INF
while left <= right:
    mid = (left+right)//2
    total = dijkstra(costs[mid])
    if total:
        ans = min(ans, costs[mid])
        right = mid-1
    else:
        left = mid+1

print(-1 if ans == INF else ans)