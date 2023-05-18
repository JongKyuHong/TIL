import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(tmp):
    global ans
    dist = [INF] * (N+1)
    dist[A] = 0
    q = [[0, A]]
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for next_node, next_cost in lst[node]:
            if next_cost > tmp:
                continue
            d = cost + next_cost
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, (d, next_node))
    return dist[B] <= C
    
N, M, A, B, C = map(int, input().split())
lst = [[] for _ in range(N+1)]
ans = INF
visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
cost = []
for _ in range(M):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
    cost.append(c)
cost.sort()
left, right = 0, len(cost)

while left < right:
    mid = (left+right) // 2
    if dijkstra(cost[mid]):
        right = mid
    else:
        left = mid + 1
print(cost[left] if left < len(cost) else -1)