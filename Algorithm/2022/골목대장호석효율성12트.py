import heapq
import sys
input = sys.stdin.readline
INF = float('inf')
def dijkstra(value):
    q = [[0, A]]
    dist = [INF]*(N+1)
    dist[A] = 0
    max_v = 0
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for next_node, next_cost in graph[now]:
            if next_cost > value:
                continue
            d = next_cost + cost
            max_v = max(max_v, next_cost)
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, (d, next_node))
    return max_v if dist[B] <= C else -1

N,M,A,B,C = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start = 0
end = C
ans = INF
while start <= end:
    mid = (start+end)//2
    target = dijkstra(mid)
    if target == -1:
        start = mid + 1
    else:
        ans = min(target, ans)
        end = mid-1
print(ans if ans != INF else -1)