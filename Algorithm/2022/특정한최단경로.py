# import sys
# input = sys.stdin.readline

# # 방향성없는 그래프, 1번에서 N번으로 최단거리 이동
# # 임의로 주어진 두 정점은 반드시 통과
# # 한번이동했던 정점, 한번 이동했던 간선 모두 다시 이동가능
# INF = sys.maxsize
# N, E = map(int, input().split()) # 정점의 갯수, 간선의 갯수
# graph = [[INF]*(N+1) for _ in range(N+1)]
# for _ in range(E):
#     a, b, c = map(int, input().split()) # c는 거리
#     # graph[a].append((b,c))
#     # graph[b].append((a,c))
#     graph[a][b] = c
#     graph[b][a] = c

# v1, v2 = map(int, input().split())

# for k in range(1,N+1):
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             if graph[i][j] > graph[i][k] + graph[k][i]:
#                 graph[i][j] = graph[i][k] + graph[k][i]

# try:
#     print(graph[1][v1]+graph[v1][v2]+graph[v2][N])
# except:
#     print(-1)

# # 시간초과 코드

import sys
import heapq
input = sys.stdin.readline

# 방향성없는 그래프, 1번에서 N번으로 최단거리 이동
# 임의로 주어진 두 정점은 반드시 통과
# 한번이동했던 정점, 한번 이동했던 간선 모두 다시 이동가능
INF = sys.maxsize
N, E = map(int, input().split()) # 정점의 갯수, 간선의 갯수
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split()) # c는 거리
    graph[a].append((b,c))
    graph[b].append((a,c))
    
v1, v2 = map(int, input().split())
res = []

def dijkstra(i):
    dist = [INF] * (N+1)
    dist[i] = 0
    q = [[0, i]]
    while q:
        now_dist, now = heapq.heappop(q)
        if dist[now] < now_dist:
            continue
        for next_node, next_dist in graph[now]:
            d = next_dist + now_dist
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, (d, next_node))

    return dist

st = dijkstra(1)
st1 = dijkstra(v1)
st2 = dijkstra(v2)

cnt = min(st[v1]+st1[v2]+st2[N],st[v2]+st2[v1]+st1[N])

print(cnt if cnt < INF else -1)