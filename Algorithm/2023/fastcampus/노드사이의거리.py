from collections import deque
import sys 
input = sys.stdin.readline
INF = float('inf')

def bfs(start, end):
    global INF
    q = deque()
    q.append((start, 0))
    visited = [0]*N
    distlst = [INF]*N
    distlst[start] = 0
    while q:
        now, cost = q.popleft()
        for node, dist in lst[now]:
            if not visited[node]:
                if distlst[node] > cost+dist:
                    visited[node] = 1
                    distlst[node] = cost+dist
                    q.append((node, cost+dist))
    return distlst[end]


N, M = map(int, input().split())

lst = [[] for _ in range(N)]
for _ in range(N-1):
    node1, node2, dist = map(int, input().split())
    lst[node2-1].append((node1-1, dist))
    lst[node1-1].append((node2-1, dist))


for _ in range(M):
    node1, node2 = map(int, input().split())
    print(bfs(node1-1, node2-1))
