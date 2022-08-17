import heapq
n,m,r = map(int, input().split())
INF = float('inf')
graph = [[]*(n+1) for _ in range(n+1)]
t = [0] + list(map(int, input().split()))
for _ in range(r):
    a,b,l = map(int, input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for end,value in graph[now]:
            c = cost + value
            if dist[end] > c:
                dist[end] = c
                heapq.heappush(q,(c, end))

res = 0
for i in range(1, n+1):
    cnt = 0
    dist = [INF]*(n+1)
    dijkstra(i)
    for j in range(1, n+1):
        if dist[j] <= m:
            cnt += t[j]
    res = max(res, cnt)
print(res)




