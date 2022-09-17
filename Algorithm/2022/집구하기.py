import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().split()) # w는 가중치
    try:
        if graph[u][1] < w:
            continue
        else:
            graph[u][1] = w
            graph[v][1] = w
    except:
        graph[u].append((v,w))
        graph[v].append((u,w))

M, x = map(int, input().split())
Mac = list(map(int, input().split()))
S, y = map(int, input().split())
Star = list(map(int, input().split()))

min_v = sys.maxsize
def dijkstra(dist):
    while q:
        now_dist, now = heapq.heappop(q)
        if dist[now] < now_dist:
            continue
        for next_node, next_dist in graph[now]:
            d = next_dist + now_dist
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q,[d, next_node])
    return dist

dist1 = [sys.maxsize] * (V+1)
q = []
for i in Mac: # 맥도날드 목록을 for문을 돌림
    q.append([0, i]) # 바로 q에 넣고 
    dist1[i] = 0 # 거리 초기화
dist1 = dijkstra(dist1) # 한번에 돌림

q = []
dist2 = [sys.maxsize] * (V+1)
for i in Star:
    q.append([0, i])
    dist2[i] = 0
dist2 = dijkstra(dist2)

for i in range(1, V+1):
    if dist1[i] and dist2[i] and dist1[i] <=x and dist2[i] <= y:
        min_v = min(min_v, dist1[i]+dist2[i])
        
print(-1 if min_v == sys.maxsize else min_v)