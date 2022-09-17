import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m, a, b, c = map(int, input().split()) # 교차로갯수, 골목개수, 시작교차로번호, 도착, 가진돈
graph = [[] for _ in range(n+1)]
costs = []
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))
    costs.append(z)

def dijkstra(mid):
    q = [[0, a]]
    dist = [INF] * (n+1)
    dist[a] = 0
    while q:
        now_dist, now = heapq.heappop(q)
        if dist[now] < now_dist:
            continue
        for next_node, next_dist in graph[now]:
            if next_dist > mid:
                continue
            d = next_dist + now_dist
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q,(d, next_node))
    return dist[b] <= c



costs.sort()
left = 0
right = len(costs)-1
ans = INF
while left <= right:
    mid = (left+right)//2
    total  = dijkstra(costs[mid])
    if total:
        ans = min(ans,costs[mid])
        right = mid - 1
    else:
        left = mid + 1


print(-1 if ans == INF else ans)


