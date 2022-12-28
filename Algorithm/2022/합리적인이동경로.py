import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split()) # 정점의 갯수n, 간선의 갯수m
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = [[0, start]]
    dist[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for next_node, next_dist in graph[now]:
            if dist[next_node] > next_dist+cost:
                dist[next_node] = next_dist+cost
                heapq.heappush(q, (next_dist+cost, next_node))
            if dist[next_node] < cost:
                dp[now] += dp[next_node]

dp = [0]*(n+1)
dist = [float('inf')]*(n+1)
dp = [0 for _ in range(n+1)]
dp[2] = 1
dijkstra(2)
print(dp[1])