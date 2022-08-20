import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

for _ in range(int(input())):
    n, d, c  = map(int, input().split()) # 컴퓨터갯수, 의존성개수, 해킹당한 컴퓨터 번호
    graph = [[] for _ in range(n+1)]
    for _ in range(d): 
        a, b, s = map(int, input().split()) # a가b를 의존, b가 감염되면 s초후에 a도 감염
        graph[b].append((a, s))

    q = [[0, c]]
    dist = [INF] * (n+1)
    dist[c] = 0
    while q:
        now_dist, now = heapq.heappop(q)
        if dist[now] < now_dist:
            continue
        for next_node, next_dist  in graph[now]:
            d = next_dist+ now_dist
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, (d, next_node))
    
    cnt = n
    max_v = 0
    print(dist,'dd')
    for i in dist[1:]:
        if i == INF:
            cnt -= 1
        else:
            max_v = max(max_v, i)
    print(cnt, max_v)