import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    k = int(input())
    room = list(map(int, input().split()))
    res = [0]*(n+1)
    
    for i in room:
        distance = [INF] * (n+1)
        distance[i] = 0
        q = [(0, i)]
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for next_node, next_dist in graph[now]:
                d = next_dist + dist
                if distance[next_node] > d:
                    distance[next_node] = d
                    heapq.heappush(q,(d, next_node))
        for j in range(1, n+1):
            res[j] += distance[j]
    minn = 0
    noww = INF
    for i in range(1, n+1):
        if noww > res[i]:
            noww = res[i]
            minn = i
    print(minn)
