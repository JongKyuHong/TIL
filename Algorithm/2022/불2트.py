from collections import deque
import sys
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(r, c):
    q = deque()
    q.append((r, c)) # r,c,거리,불인지 지훈인지 불 0 지훈 1
    visited[r][c] = 1
    while q:
        r, c= q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < a and 0 <= nc < b and graph[nr][nc] != '#':
                if visited[nr][nc] == INF:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                else:
                    if visited[nr][nc] > visited[r][c] + 1:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc))

def find_exit(r, c):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < a and 0 <= nc < b and graph[nr][nc] != '#':
                if visited[nr][nc] > visited[r][c] + 1:
                    if nr == 0 or nr == a-1 or nc == 0 or nc == b-1:
                        return visited[r][c] + 1
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
    return 'IMPOSSIBLE'


a, b = map(int, input().split())
jihun = []
fire = []
graph = []
for i in range(a):
    data = list(input())
    for j in range(b):
        if data[j] == 'J':
            jihun.append((i, j))
        elif data[j] == 'F':
            fire.append((i, j))
    graph.append(data)
if jihun[0][0] == 0 or jihun[0][0] == a-1 or jihun[0][1] == 0 or jihun[0][1] == b-1:
    print(1)
    exit()
    
INF = float('inf')
visited = [[INF for _ in range(b)] for _ in range(a)]

for i, j in fire:
    bfs(i, j)

print(find_exit(jihun[0][0],jihun[0][1]))
# #벽, .지나가는공간, J지훈이 초기위치, F불이난 공간
