from collections import deque
import heapq
import sys 
input = sys.stdin.readline
INF = float('inf')

def dijstra(start):
    q = []
    heapq.heappush(q, (0, start, [start]))
    dist = [INF]*(N+1)
    dist[start] = 0
    while q:
        cost, node, path = heapq.heappop(q)
        for next_cost, next_node in lst[node]:
            val = cost + next_cost
            if val < dist[next_node]:
                dist[next_node] = val
                heapq.heappush(q, (val, next_node, path + [next_node]))
    return dist

def bfs():
    q = deque()
    q.append(D)
    while q:
        now = q.popleft()
        if now == S:
            continue
        for prev_cost, prev_node in reverse_lst[now]:
            if dist[now] == dist[prev_node] + prev_cost:
                
                

while 1:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())
    lst = [[] for _ in range(N+1)]
    reverse_lst = [[] for _ in range(N+1)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        lst[U].append((P, V))
        reverse_lst[V].append((P, U))    
    dist = dijstra(S)
    bfs(dist)
    
    



# 처음에 할때 최단 거리가 나온다.
# 최단거리와 같은 경우를 모아서 paths에다가 path모음
# 걔네들을 한번에 visited처리를함
# 그 다음에 최단 거리를 찾음, 있으면 출력하고, 없으면 -1