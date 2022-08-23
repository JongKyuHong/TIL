import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
graph2 = [[0 for _ in range(n+1)] for _ in range(n+1)]
a, b, k, g = map(int, input().split()) # 상근이가 배달 시작하는교차로, 마치는교차로, 상근출발시간 - 고돌라 출발시간, 고돌라가 방문하는 교차로 갯수
G = list(map(int, input().split()))
for _ in range(m):
    u, v, l = map(int, input().split())
    graph[u].append((v,l))
    graph[v].append((u,l))
    graph2[u][v] = l
    graph2[v][u] = l

kings_load = [[[-1,-1] for _ in range(n+1) ] for _ in range(n+1)]
kings_v = 0
prev = 0

for i in range(1, g):
    before = G[i-1]
    node = G[i]
    kings_load[before][node] = prev, prev + graph2[before][node]
    kings_load[node][before] = prev, prev + graph2[before][node]
    prev += graph2[before][node]

q = [[k, a]]   # , [a]
dist = [sys.maxsize] * (n+1)
dist_path = [[] for _ in range(n+1)]
dist[a] = k

while q:
    now_dist, now = heapq.heappop(q) #  , path
    if dist[now] < now_dist:
        continue
    for next_node, next_dist in graph[now]:
        my_start = now_dist
        king_start, king_end = kings_load[now][next_node]
        if king_start <= my_start <= king_end:
            my_start = king_end

        if dist[next_node] > my_start + next_dist:
            dist[next_node] = my_start + next_dist
            heapq.heappush(q,(my_start + next_dist, next_node))

print(dist[b]-k)
