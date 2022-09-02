import heapq
import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
INF = float('inf')
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))


def dijkstra(start):
    INF = float('inf')
    q = [(0, start)]
    distance = [INF] * (n+1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, next_dist in graph[now]:
            if distance[next_node] > next_dist + dist:
                distance[next_node] = next_dist + dist
                heapq.heappush(q, (distance[next_node],next_node))
    return distance


res = [0]*(n+1)
for i in range(1, n+1):
    d = dijkstra(i)
    res[i] += d[x]
    d = dijkstra(x)
    res[i] += d[i]
print(max(res))
